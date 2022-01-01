from ets_mysql_lib import MysqlConnection as mc
from datetime import datetime
from lxml import etree
import argparse
import config
import queries
import uuid
import re
import os
from paramiko import SSHClient
from scp import SCPClient

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect('10.100.172.55', username='a_kukeev',
            password='kY5J66(Rv9rw', look_for_keys=False)
shell = ssh.invoke_shell()


UPLOAD_DIR = '/upl/srv/www/sectionks/data/upload8'


def testing():
    print('Тестировать пока нечего')


def get_cancel_shape(file=None,path=None):
    path = '/opt/python_scripts/send_modification/files/'
    file = 'epprotocolcancel.xml'
    
    with SCPClient(shell.get_transport()) as scp:
        scp.get(os.path.join(path,file), './files')



def put_file(file=None, path=UPLOAD_DIR):
    # path = '/home/a_kukeev'
    file = './files/a_kukeev_test_file.txt'
    shell.send('sudo su - application')
    shell.send('sudo su - application')
    # with SCPClient(shell.get_transport()) as scp:
    #     scp.put(file, path)

def send_packet(guid, uri, type_id, status, packet_id):
    cn44 = mc(connection=mc.MS_44_1_CONNECT)
    print('Отправка пакета.')
    if status == '2' and namespace.manual is True:
        status = '12'
    with cn44.open():
        cn44.execute_query(queries.insert_packet.format(
            guid, uri, type_id, status, packet_id))


def create_new_cancel_packet(filename, uri):
    # переходим в корневой каталог аплоадов
    os.chdir('/upl/srv/www/sectionks/')
    print('Создание нового пакета отмены.')
    guid = str(uuid.uuid4())  # генерируем новый guid
    prefix = re.match('.*(?=/20)', uri)  # извлекаем путь аплоада
    if prefix:
        prefix = prefix.group(0)
    # генерирует имя каталога с текущей датой
    directory = '{0}/{1}'.format(prefix,
                                 datetime.strftime(datetime.now(), '%Y-%m-%d'))
    if not os.path.exists(directory):
        os.makedirs(directory)  # создаем каталог, если не существует
    new_file = '{0}/{1}'.format(directory, guid)
    root = etree.parse(filename, etree.XMLParser(
        encoding='utf-8', recover=True, huge_tree=True))
    # меняем guid в пакете
    root.xpath('//none:index/none:id',
               namespaces=config.namespaces)[0].text = guid
    root.xpath('//none:index/none:createDateTime', namespaces=config.namespaces)[
        0].text = str(datetime.strftime(datetime.now(), '%Y-%m-%dT%X+03:00'))
    root = etree.tounicode(root)
    with open(new_file, 'w', encoding='utf-8') as f2:  # пишем в файл
        f2.write(root)

    return new_file, guid


def copy_packet_with_new_guid(uri):
    # переходим в корневой каталог аплоадов
    os.chdir('/upl/srv/www/sectionks/')
    print('Копирование пакета с новым guid.')
    guid = str(uuid.uuid4())  # генерируем новый guid
    prefix = re.match('.*(?=/20)', uri)  # извлекаем путь аплоада
    if prefix:
        prefix = prefix.group(0)
    # генерирует имя каталога с текущей датой
    directory = '{0}/{1}'.format(prefix,
                                 datetime.strftime(datetime.now(), '%Y-%m-%d'))
    if not os.path.exists(directory):
        os.makedirs(directory)  # создаем каталог, если не существует
    new_file = '{0}/{1}'.format(directory, guid)
    root = etree.parse(uri, etree.XMLParser(
        encoding='utf-8', recover=True, huge_tree=True))
    # меняем guid в пакете
    root.xpath('//none:index/none:id',
               namespaces=config.namespaces)[0].text = guid
    root = etree.tounicode(root)
    with open(new_file, 'w', encoding='utf-8') as f2:  # пишем в файл
        f2.write(root)

    return new_file, guid  # возвращаем новый uri


def modification_ea(regnum, uri, type, packet_id):
    print('{} {}\n'
          'Модификация протокола.'.format(regnum, type))
    new_uri, guid = copy_packet_with_new_guid(uri)
    root = etree.parse(new_uri, etree.XMLParser(
        encoding='utf-8', recover=True, huge_tree=True))

    print('Формирование пакета модификации.')
    with sql44.open():
        last_success_packet = sql44.execute_query(
            queries.check_last_success_packet.format(packet_id))
    if last_success_packet:
        last_success_packet_uri = last_success_packet[0][0]
        sroot = etree.parse(last_success_packet_uri, etree.XMLParser(
            encoding='utf-8', recover=True, huge_tree=True))
    else:
        print('Не найден успешный отправленный {} по закупке {}. Модификация не требуется.'.format(
            type, regnum))
        exit(0)

    #  Проверка успешно отправленного пакета
    check_success_modification = sroot.find(
        '//none:data/fcs:modification', namespaces=config.namespaces)
    check_new_modification = root.find(
        '//none:data/fcs:modification', namespaces=config.namespaces)
    if not check_new_modification:
        if check_success_modification is None:
            root = add_modification_ea(root, '1')
        else:
            current_number = sroot.find(
                '//none:data/fcs:modification/fcs:modificationNumber', namespaces=config.namespaces).text
            root = add_modification_ea(root, str(int(current_number) + 1))

        parent_protocol = sroot.find(
            '//none:data/fcs:protocolNumber', namespaces=config.namespaces).text
        pp = etree.Element(
            '{http://zakupki.gov.ru/oos/types/1}parentProtocolNumber', nsmap=config.namespaces)
        pp.text = parent_protocol
        root.find('//none:data/fcs:protocolNumber',
                  namespaces=config.namespaces).addnext(pp)

    else:
        current_number = sroot.find(
            '//none:data/fcs:modification/fcs:modificationNumber', namespaces=config.namespaces).text
        root.find('//none:data/fcs:modification/fcs:modificationNumber',
                  namespaces=config.namespaces).text = str(int(current_number) + 1)

        parent_protocol = sroot.find(
            '//none:data/fcs:protocolNumber', namespaces=config.namespaces).text
        root.xpath('//none:data/fcs:parentProtocolNumber',
                   namespaces=config.namespaces)[0].text = parent_protocol

    protocol_number = re.sub(
        '.$', str(int(re.search('.$', parent_protocol).group(0)) + 1), parent_protocol)
    root.xpath('//none:data/fcs:protocolNumber',
               namespaces=config.namespaces)[0].text = protocol_number
    root = etree.tounicode(root)

    with open(new_uri, 'w', encoding='utf-8') as file:
        file.write(root)

    send_packet(guid, new_uri, 'ip.typeid', 2, packet_id)

    return guid


def add_modification_ea(root, number):
    decision_date = etree.Element(
        '{http://zakupki.gov.ru/oos/types/1}decisionDate', nsmap=config.namespaces)
    decision_date.text = datetime.strftime(datetime.today(), '%Y-%m-%dT%X')
    responsible_decision = etree.Element(
        '{http://zakupki.gov.ru/oos/types/1}responsibleDecision', nsmap=config.namespaces)
    responsible_decision.insert(0, decision_date)
    reason = etree.Element(
        '{http://zakupki.gov.ru/oos/types/1}reason', nsmap=config.namespaces)
    reason.insert(0, responsible_decision)
    info = etree.Element(
        '{http://zakupki.gov.ru/oos/types/1}info', nsmap=config.namespaces)
    info.text = 'По решению заказчика'
    modification_number = etree.Element(
        '{http://zakupki.gov.ru/oos/types/1}modificationNumber', nsmap=config.namespaces)
    modification_number.text = number
    modification = etree.Element(
        '{http://zakupki.gov.ru/oos/types/1}modification', nsmap=config.namespaces)
    modification.insert(0, modification_number)
    modification.insert(1, info)
    modification.insert(2, reason)
    root.xpath('//none:data/fcs:protocolLot',
               namespaces=config.namespaces)[0].addprevious(modification)

    return root


def modification_eakr(regnum, uri, type, packet_id):
    print('{} {}\n'
          'Модификация протокола.'.format(regnum, type))
    new_uri, guid = copy_packet_with_new_guid(uri)
    root = etree.parse(new_uri, etree.XMLParser(
        encoding='utf-8', recover=True, huge_tree=True))
    print('Формирование пакета модификации.')
    # проверяем, не модификация ли уже
    modification = root.find(
        '//none:data/pprf615:modificationInfo', namespaces=config.namespaces)
    if not modification:
        # вставляем тэг modificationInfo
        decision_date = etree.Element(
            '{http://zakupki.gov.ru/oos/pprf615types/1}decisionDate', nsmap=config.namespaces)
        decision_date.text = datetime.strftime(datetime.today(), '%Y-%m-%d')
        responsible_decision_info = etree.Element(
            '{http://zakupki.gov.ru/oos/pprf615types/1}responsibleDecisionInfo', nsmap=config.namespaces)
        responsible_decision_info.insert(0, decision_date)
        reason_info = etree.Element(
            '{http://zakupki.gov.ru/oos/pprf615types/1}reasonInfo', nsmap=config.namespaces)
        reason_info.insert(0, responsible_decision_info)
        info = etree.Element(
            '{http://zakupki.gov.ru/oos/pprf615types/1}info', nsmap=config.namespaces)
        info.text = 'По решению заказчика'
        modification_info = etree.Element(
            '{http://zakupki.gov.ru/oos/pprf615types/1}modificationInfo', nsmap=config.namespaces)
        modification_info.insert(0, info)
        modification_info.insert(1, reason_info)
        root.find('//none:data/pprf615:attachmentsInfo',
                  namespaces=config.namespaces).addnext(modification_info)

    current_version = root.xpath(
        '//none:data/ns0:versionNumber', namespaces=config.namespaces)
    if current_version:
        current_version = current_version[0].text
        new_version = str(int(current_version) + 1)
        root.xpath('//none:data/pprf615:versionNumber',
                   namespaces=config.namespaces)[0].text = new_version
    else:
        version_number = etree.Element(
            '{http://zakupki.gov.ru/oos/pprf615types/1}versionNumber', nsmap=config.namespaces)
        version_number.text = '2'
        root.find('//none:data',
                  namespaces=config.namespaces).insert(0, version_number)

    root = etree.tounicode(root)
    with open(new_uri, 'w', encoding='utf-8') as file:
        file.write(root)

    send_packet(guid, new_uri, 'ip.typeid', 2, packet_id)

    return guid


def modification_procedures(regnum, uri, type, packet_id):
    print('{} {}\n'
          'Модификация протокола.'.format(regnum, type))
    new_uri, guid = copy_packet_with_new_guid(uri)
    root = etree.parse(new_uri, etree.XMLParser(
        encoding='utf-8', recover=True, huge_tree=True))

    print('Формирование пакета модификации.')
    # проверяем, не модификация ли уже
    modification = root.find(
        '//none:data/ns0:modificationInfo', namespaces=config.namespaces)
    if not modification:
        # вставляем тэг modificationInfo
        decision_date = etree.Element('decisionDate')
        decision_date.text = datetime.strftime(datetime.today(), '%Y-%m-%d')
        responsible_decision_info = etree.Element('responsibleDecisionInfo')
        responsible_decision_info.insert(0, decision_date)
        reason_info = etree.Element('reasonInfo')
        reason_info.insert(0, responsible_decision_info)
        info = etree.Element('info')
        info.text = 'По решению заказчика'
        modification_info = etree.Element('modificationInfo')
        modification_info.insert(0, info)
        modification_info.insert(1, reason_info)
        root.find('//none:data/ns0:attachmentsInfo',
                  namespaces=config.namespaces).addnext(modification_info)

    current_version = root.xpath(
        '//none:data/ns0:versionNumber', namespaces=config.namespaces)[0].text
    new_version = str(int(current_version) + 1)
    root.xpath('//none:data/ns0:versionNumber',
               namespaces=config.namespaces)[0].text = new_version

    external_id = root.xpath('//none:data/ns0:externalId',
                             namespaces=config.namespaces)[0].text
    new_external_id = re.sub(
        '.$', str(int(re.search('.$', external_id).group(0)) + 1), external_id)
    root.xpath('//none:data/ns0:externalId',
               namespaces=config.namespaces)[0].text = new_external_id
    root.xpath('//none:data/ns0:commonInfo/ns0:docNumberExternal',
               namespaces=config.namespaces)[0].text = new_external_id

    root = etree.tounicode(root)

    with open(new_uri, 'w', encoding='utf-8') as file:
        file.write(root)

    send_packet(guid, new_uri, 'ip.typeid', 2, packet_id)

    return guid


def cancel_eakr(regnum, uri, type, packet_id):
    print('{} {}\n'
          'Отмена протокола.'.format(regnum, type))
    new_uri, guid = create_new_cancel_packet(config.eakr_cancel_file, uri)
    old_root = etree.parse(uri, etree.XMLParser(
        encoding='utf-8', recover=True, huge_tree=True))
    # забираем теги из отменяемого пакета
    object_id = old_root.xpath(
        '//none:index/none:objectId', namespaces=config.namespaces)[0].text
    doc_number = old_root.xpath(
        '//none:data/pprf615:commonInfo/pprf615:docNumberExternal', namespaces=config.namespaces)[0].text
    create_date = old_root.xpath(
        '//none:data/pprf615:commonInfo/pprf615:createDate', namespaces=config.namespaces)[0].text
    sign_date = old_root.xpath(
        '//none:data/pprf615:commonInfo/pprf615:signDate', namespaces=config.namespaces)[0].text
    print('Формирование пакета отмены.')
    while True:
        decision_date = input(
            'Введите дату принятия решения КО (YYYY-MM-DD)\n')
        if re.match('\d{4}-\d{2}-\d{2}', decision_date):
            break
        else:
            print('Неверный формат')
            continue
    root = etree.parse(new_uri)
    root.xpath('//none:index/none:objectId',
               namespaces=config.namespaces)[0].text = object_id
    root.xpath('//none:data/pprf615:commonInfo/pprf615:purchaseNumber',
               namespaces=config.namespaces)[0].text = object_id
    root.xpath('//none:data/pprf615:commonInfo/pprf615:docNumberExternal',
               namespaces=config.namespaces)[0].text = doc_number
    root.xpath('//none:data/pprf615:commonInfo/pprf615:canceledProtocolNumber',
               namespaces=config.namespaces)[0].text = doc_number
    root.xpath('//none:data/pprf615:commonInfo/pprf615:createDate',
               namespaces=config.namespaces)[0].text = create_date
    root.xpath('//none:data/pprf615:commonInfo/pprf615:signDate',
               namespaces=config.namespaces)[0].text = sign_date
    root.xpath('//none:data/pprf615:cancelReason/pprf615:reasonInfo/pprf615:responsibleDecisionInfo/pprf615:decisionDate',
               namespaces=config.namespaces)[0].text = decision_date

    root = etree.tounicode(root)
    with open(new_uri, 'w', encoding='utf-8') as file:
        file.write(root)

    send_packet(guid, new_uri, 77, 2, packet_id)

    return guid


def cancel_procedures(regnum, uri, type, packet_id):
    prolongation = None
    print('{} {}\n'
          'Отмена протокола.'.format(regnum, type))
    new_uri, guid = create_new_cancel_packet(config.procedure_cancel_file, uri)
    old_root = etree.parse(uri, etree.XMLParser(
        encoding='utf-8', recover=True, huge_tree=True))
    # забираем теги из отменяемого пакета
    with sql44.open():
        type_code = sql44.execute_query(
            queries.get_type_query.format(packetId))
    if type_code:
        type_code = list(type_code[0])[0]

    object_id = old_root.xpath(
        '//none:index/none:objectId', namespaces=config.namespaces)[0].text
    doc_number = old_root.xpath(
        '//none:data/ns0:commonInfo/ns0:docNumberExternal', namespaces=config.namespaces)[0].text
    create_date = old_root.xpath(
        '//none:data/ns0:commonInfo/ns0:publishDTInETP', namespaces=config.namespaces)[0].text
    sign_date = old_root.xpath(
        '//none:data/ns0:commonInfo/ns0:signDT', namespaces=config.namespaces)[0].text
    href = old_root.xpath(
        '//none:data/ns0:commonInfo/ns0:hrefExternal', namespaces=config.namespaces)[0].text
    if old_root.xpath('//none:data/ns0:afterProlongation', namespaces=config.namespaces):
        prolongation = old_root.xpath(
            '//none:data/ns0:afterProlongation', namespaces=config.namespaces)[0].text
    print('Формирование пакета отмены.')
    auth_name = input('Введите наименование КО\n')
    doc_name = input('Введите наименование документа\n')
    ko_doc_number = input('Введите номер документа\n')
    while True:
        decision_date = input(
            'Введите дату принятия решения КО (YYYY-MM-DD)\n')
        if re.match('\d{4}-\d{2}-\d{2}', decision_date):
            break
        else:
            print('Неверный формат')
            continue

    root = etree.parse(new_uri)
    root.xpath('//none:index/none:objectId',
               namespaces=config.namespaces)[0].text = object_id
    root.xpath('//none:data/ns0:externalId',
               namespaces=config.namespaces)[0].text = doc_number
    root.xpath('//none:data/ns0:commonInfo/ns0:purchaseNumber',
               namespaces=config.namespaces)[0].text = object_id
    root.xpath('//none:data/ns0:commonInfo/ns0:publishDTInETP',
               namespaces=config.namespaces)[0].text = create_date
    root.xpath('//none:data/ns0:commonInfo/ns0:signDate',
               namespaces=config.namespaces)[0].text = sign_date
    root.xpath('//none:data/ns0:commonInfo/ns0:hrefExternal',
               namespaces=config.namespaces)[0].text = href
    root.xpath('//none:data/ns0:commonInfo/ns0:canceledProtocolType',
               namespaces=config.namespaces)[0].text = type_code
    root.xpath('//none:data/ns0:commonInfo/ns0:canceledProtocolNumber',
               namespaces=config.namespaces)[0].text = doc_number

    root.xpath('//none:data/ns0:cancelReasonInfo/ns0:reasonInfo/ns0:authorityPrescriptionInfo/ns0:externalPrescription/ns0:authorityName',
               namespaces=config.namespaces)[0].text = auth_name
    root.xpath('//none:data/ns0:cancelReasonInfo/ns0:reasonInfo/ns0:authorityPrescriptionInfo/ns0:externalPrescription/ns0:prescriptionProperty/cmn:docName',
               namespaces=config.namespaces)[0].text = doc_name
    root.xpath('//none:data/ns0:cancelReasonInfo/ns0:reasonInfo/ns0:authorityPrescriptionInfo/ns0:externalPrescription/ns0:prescriptionProperty/cmn:docNumber',
               namespaces=config.namespaces)[0].text = ko_doc_number
    root.xpath('//none:data/ns0:cancelReasonInfo/ns0:reasonInfo/ns0:authorityPrescriptionInfo/ns0:externalPrescription/ns0:prescriptionProperty/cmn:docDate',
               namespaces=config.namespaces)[0].text = decision_date
    if prolongation == 'true':
        root.xpath('//none:data/ns0:afterProlongation',
                   namespaces=config.namespaces)[0].text = prolongation

    root = etree.tounicode(root)
    with open(new_uri, 'w', encoding='utf-8') as file:
        file.write(root)

    send_packet(guid, new_uri, 187, 2, packet_id)

    return guid


def create_parser():
    """
    Парсер аргументов командной строки
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('packetId', type=str, help='id пакета')
    parser.add_argument('-c', '--cancel', action='store_true',
                        help='Собрать пакет отмены')
    parser.add_argument('-t', '--test', action='store_true',
                        help='Режим тестирования')
    parser.add_argument('-m', '--manual', action='store_true',
                        help='В статус "ручная отправка"')

    return parser


def emergency_exit(text):
    print(text)
    exit(2)


if __name__ == '__main__':

    # parser = create_parser()
    # namespace = parser.parse_args()
    # packetId = str(namespace.packetId)
    # sql44 = mc(connection=mc.MS_44_1_CONNECT)

    # if namespace.test:
    #     testing()
    #     exit(0)

    # if not re.match('\d{0,10}', packetId):
    #     emergency_exit('Некорректный номер пакета!')
    # with sql44.open():
    #     packet = sql44.execute_query(queries.get_packet_info_query.format(packetId, ','.join(config.ea_protocols)))
    #     if packet:
    #         packet = list(packet[0])
    #         if namespace.cancel:
    #             exit(0)
    #         else:
    #             guid = modification_ea(packet[0], packet[2], packet[1], packetId)
    #     else:
    #         packet = sql44.execute_query(queries.get_packet_info_query.format(packetId, ','.join(config.eakr_protocols)))
    #         if packet:
    #             packet = list(packet[0])
    #             if namespace.cancel:
    #                 guid = cancel_eakr(packet[0], packet[2], packet[1], packetId)
    #             else:
    #                 guid = modification_eakr(packet[0], packet[2], packet[1], packetId)
    #         else:
    #             packet = sql44.execute_query(queries.get_packet_info_query.format(packetId, ','.join(config.procedures_protocols)))
    #             if packet:
    #                 packet = list(packet[0])
    #                 if namespace.cancel:
    #                     guid = cancel_procedures(packet[0], packet[2], packet[1], packetId)
    #                 else:
    #                     guid = modification_procedures(packet[0], packet[2], packet[1], packetId)
    #             else:
    #                 if namespace.cancel:
    #                     emergency_exit('Не умею отменять пакет данного типа')
    #                 else:
    #                     emergency_exit('Не умею модифицировать пакет данного типа')

    # if guid:
    #     print('Пакет отправлен с guid = {}'.format(guid))

    # get_cancel_shape()
    put_file()
