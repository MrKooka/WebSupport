""""
Создан: 05.12.2017
Автор: Белим С.
belim@etpz.ru

Модуль предоставляет функционал для работы с БД MYSQL
Требует установленного mysql.connector
https://dev.mysql.com/downloads/connector/python/
"""

import re
import mysql.connector
from contextlib import contextmanager as _contextmanager
from collections import namedtuple as _namedtuple

NULL = 'null'

def value_former(value):
    """Метод для формирования корректной текстовой строки для вставки в sql запрос"""
    return "'" + str(value).replace('\'', '\\\'') + "'"

class MysqlConnection:
    """Класс для работы с MYSQL"""

    # определяем подключения, которые могут использоваться как значение connection при инициации MysqlConnection
    MS_DEF_CONNECT = 'user', '', 'localhost', 'database', 3306
    MS_BOT_CONNECT = 'sbelim', '', '192.168.135.69', 'ets_bot', 3306
#    MS_KASPERSKY_CONNECT = 'sbelim', '', '192.168.135.69', 'kasperskyDb', 3306
#    MS_KASPERSKY_CONNECT = 'kaspersky_user', '', 'localhost', 'kaspersky_db', 3306
    MS_KASPERSKY_CONNECT = 'belim', '', '10.250.250.2', 'kaspersky_db', 4355
    MS_CRYPTO_CONNECT = 'sbelim', '', '192.168.135.69', 'crypto_bd', 3306
    MS_44_1_CONNECT = 'a_kukeev', 'tFA6Up7MrB', '10.11.0.1', 'sectionks', 4301
    MS_44_2_CONNECT = 'belim', '', '10.100.172.21', 'sectionks', 3306
    MS_94_1_CONNECT = 'application', '', '10.100.172.22', 'auction', 3306
    MS_44_LOG_CONNECT = 'belim', '', '10.250.250.2', 'sectionks_log', 4306
    MS_94_LOG_CONNECT = 'duty', '', '10.250.250.2', 'auction-log', 4305
    MS_FTEST_CONNECT = 'developer', '', '10.99.172.36', 'sectionks', 3306

    MS_223_ZK_CONNECT = 'application', '', '10.100.172.44', '223zk', 3306
    MS_223_ZP_CONNECT = 'application', '', '10.100.172.44', '223zp', 3306
    MS_223_EK_CONNECT = 'application', '', '10.100.172.44', '223ek', 3306
    MS_223_EA1_CONNECT = 'application', '', '10.100.172.44', '223ea1', 3306
    MS_223_EA2_CONNECT = 'application', '', '10.100.172.44', '223ea2', 3306    

    MS_223_SMSP_EA_CONNECT = 'application', '', '10.100.172.67', '223smsp_ea', 3306
    MS_223_SMSP_EK_CONNECT = 'application', '', '10.100.172.67', '223smsp_ek', 3306
    MS_223_SMSP_ZK_CONNECT = 'application', '', '10.100.172.67', '223smsp_zk', 3306
    MS_223_SMSP_ZP_CONNECT = 'application', '', '10.100.172.67', '223smsp_zp', 3306

    MS_223_EA1_TRADE_CONNECT = 'application', '', '10.100.172.46', '223trade_ea1', 3306
    MS_223_EA2_TRADE_CONNECT = 'application', '', '10.100.172.46', '223trade_ea2', 3306
    
    MS_223_SMSP_EA_TRADE_CONNECT = 'application', '', '10.100.172.69', '223trade_smsp_ea', 3306

    MS_223_ORGANIZATION_CONNECT = 'application', '', '10.100.172.44', 'organization', 3306

    MS_CERT_INFO_CONNECT = 'belim', '', 'localhost', 'certificate_info', 3306
    MS_223_CATALOG_CONNECT = 'application', '', '10.100.172.1', 'sectionks_catalog_223', 3306
#    MS_CERT_INFO_CONNECT = 'sbelim', '', '192.168.135.69', 'certificate_info', 3306

    MS_44_NEW_PROCEDURES_CONTRACT_CONNECT = 'application', '', '10.100.172.140', 'contract_44', 3306
    MS_44_NEW_PROCEDURES_CATALOG_CONNECT = 'application', '', '10.100.172.140', 'catalog_44', 3306
    MS_44_NEW_PROCEDURES_CLARIFICATION_CONNECT = 'application', '', '10.100.172.140', 'clarification_44', 3306

    MS_44_EDK_CONNECT = 'application', '', '10.100.172.136', '44edk', 3306
    MS_44_EK_CONNECT = 'application', '', '10.100.172.136', '44ek', 3306
    MS_44_KOU_CONNECT = 'application', '', '10.100.172.136', '44kou', 3306
    MS_44_ZK_CONNECT = 'application', '', '10.100.172.136', '44zk', 3306
    MS_44_ZP_CONNECT = 'application', '', '10.100.172.136', '44zp', 3306

    MS_FTEST_EDK_CONNECT = 'developer', '', '10.99.172.55', '44edk', 43136
    MS_FTEST_EK_CONNECT = 'developer', '', '10.99.172.55', '44ek', 43136
    MS_FTEST_KOU_CONNECT = 'developer', '', '10.99.172.55', '44kou', 43136
    MS_FTEST_ZK_CONNECT = 'developer', '', '10.99.172.55', '44zk', 43136
    MS_FTEST_ZP_CONNECT = 'developer', '', '10.99.172.55', '44zp', 43136

    MS_EDO_CONNECT = 'application', '', '10.250.250.2', 'edo', 4322
    MS_EDO_REPLIC_CONNECT = 'application', '', '10.100.190.20', 'edo', 4336

    MS_SUPPORT_UNION_CONNECT = 'dbadmin', '', '10.100.172.66', 'sectionks', 3306 

    def __init__(self, **kwargs):
        """Инициализация подключения
        Аргументы:
        user
            :: пользователь
            :: DEFAULT: user
        password
            :: пароль
            :: DEFAULT: password
        host
            :: хост
            :: DEFAULT: localhost
        database
            :: база данных
            :: DEFAULT: database
        port
            :: порт
            :: DEFAULT: 3306
        connection
            :: использовать предопределенное подключение
        """

        # определяем подключение и курсор в __init__
        self._cnx = False
        self._mysql_сur = False

        # параметры для подключения в необходимом порядке
        c_keys = 'user', 'password', 'host', 'database', 'port'

        # namedtuple для работы с подключениями
        c_connection_keys = _namedtuple('CONNECTION_DATA', c_keys)

        # если указан параметр connection, то в _c_data возвращаем значение указанного ключа connection
        if 'connection' in kwargs.keys():
            _c_data = list(kwargs['connection'])
        # если не указан, то берем по умолчанию MS_DEF_CONNECT
        else:
            _c_data = list(self.MS_DEF_CONNECT)

        # изменяем все элементы, которые указаны вручную
        for num, key in enumerate(c_keys):
            if key in kwargs.keys():
                _c_data[num] = kwargs[key]

        # распаковываем список элементов в CONNECTION
        self._CONNECTION = c_connection_keys(*_c_data)

    def __str__(self):
        return str('(%s: %s, CONNECTED=%s)' % (self.__class__.__name__, self._CONNECTION, bool(self._cnx)))

    def connect(self):
        """Метод подключения к БД"""
        # подключаемся
        self._cnx = mysql.connector.connect(user=self._CONNECTION.user,
                                            password=self._CONNECTION.password,
                                            host=self._CONNECTION.host,
                                            database=self._CONNECTION.database,
                                            port=self._CONNECTION.port)

        return self

    @_contextmanager
    def open(self):
        """Метод для использования в контекстном менеджере"""
        # подключаемся
        self.connect()
        # возвращаем подключение
        yield self
        # после всех действий не забываем закрыть
        self.disconnect()

    def execute_query(self, query, *args, from_file=False, named=False, dicted=False):
        """Метод выполнения запросов к БД

        query ::
            запрос
        *args ::
            подстановки, указанные в запросе через %s
        from_file ::
            True если требуется query ссылка на файл (по умолчанию FALSE)
        named ::
            True если требуется возвращать строки именованным списком (по умолчанию FALSE)
        dicted ::
            True если требуется возвращать строки словарями (по умолчанию FALSE)
        При выполнении запроса SELECT метод возвращает кортеж данных
        При выполнении UPDATE, INSERT, DELETE возвращает None
        """

        if not self._cnx:
            raise Exception('Connection not exists')

        # определяем курсор (для именованных или dictionary требуется определить с dictionary)
        self._mysql_сur = self._cnx.cursor(dictionary=named or dicted)

        if from_file:
            with open(query, encoding="cp1251") as query_file:
                query = query_file.read()

        # убираем пробелы из начала запроса
        query = query.lstrip()

        # выполнение запроса
        if args:
            self._mysql_сur.execute(query, tuple(args))
        else:
            self._mysql_сur.execute(query)

        # если SELECT, то надо вернуть данные
        if query.lower().startswith('select'):

            # получаем данные
            mysql_out = self._mysql_сur.fetchall()

            # если указано возвращать строки именованными списками, то их и вернем
            if named and mysql_out:

                sorted_keys = mysql_out[0].keys()
                tmp_mysql_out = []
                Row = _namedtuple('Row', sorted_keys)

                for row in mysql_out:
                    tmp_mysql_out.append(Row(*(row[key] for key in sorted_keys)))

                mysql_out = tmp_mysql_out

            return tuple(mysql_out)

        # если UPDATE, INSERT, DELETE, то коммитим и возвращаем None
        elif query.lower().startswith('update') \
                or query.lower().startswith('insert') \
                or query.lower().startswith('delete'):

            self._cnx.commit()
            return None

    def disconnect(self):
        """Метод отключения от БД"""
        try:
            self._mysql_сur.close()
        except:
            pass

        self._cnx = False
        self._mysql_сur = False


def get_query_top(query, from_file=False):
    """Метод возвращает названия столбцов из запроса
    query -- файл или текст запроса
    Метод корректно обрабатывает заголовки следующего вида:
    | proc.`Заказчик`(,)
    | proc.zak (as) ('`)Заказчик('`)(,)
    В двойные кавычки оборачивать наименование столбца нельзя, они зарезервированы только под использование внутри наименования
    В шапке разрешается комментировать строки выборки следующим образом:
    |(возможен 1 пробел)-- proc.`Заказчик`
    Метод возвращает кортеж из заголовков.
    """

    if from_file:
        with open(query, encoding="cp1251") as query_file:
            query = query_file.read()

    # ищем шапку запроса
    first_select = re.search(r"SELECT.*?FROM", query, re.IGNORECASE | re.DOTALL)
    # и выбираем из нее заголовки
    tops = re.findall(r"^ [^(--)].*?(\.|(AS )){1}(['`])([^'`]+?)\3[,]*$", first_select.group(0),
                      re.IGNORECASE | re.DOTALL | re.MULTILINE)
    # формируем из заголовков топ для страницы
    return tuple(x[3] for x in tops)
