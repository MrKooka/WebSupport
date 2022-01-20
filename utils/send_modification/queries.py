get_packet_info_query = '''
SELECT ip.regNumber, ipt.title, ip.contentUri FROM sectionks.oosIntegrationPacket ip
  JOIN sectionks.oosIntegrationPacketType ipt ON ip.typeId = ipt.id
  WHERE ip.id = {}
  AND ip.typeId IN ({})
  ;
'''

insert_packet = '''INSERT INTO oosIntegrationPacket 
(partnerFrom,
partnerTo,
guid,
regNumber,
objectId,
source,
createDateTime,
receiveDateTime,
contentUri,
indexNum,
typeId,
packetStatusId,
mode)
  SELECT
    ip.partnerFrom,
    ip.partnerTo,
    '{}', 
    ip.regNumber,
    ip.objectId, 
    ip.source,
    NOW(),
    NOW(),
    '{}', 
    ip.indexNum,
    {}, 
    {}, 
    ip.mode
  FROM oosIntegrationPacket ip
  WHERE ip.id = {}
;'''

get_type_query = '''
SELECT ipt.code FROM sectionks.oosIntegrationPacket ip 
  JOIN sectionks.oosIntegrationPacketType ipt ON ip.typeId = ipt.id
WHERE ip.id = {};
'''

check_last_success_packet = '''
SELECT ip.contentUri FROM sectionks.oosIntegrationPacket ip 
  WHERE ip.typeId = (SELECT typeId FROM sectionks.oosIntegrationPacket WHERE id = {0})
  AND ip.regNumber = (SELECT regNumber FROM sectionks.oosIntegrationPacket WHERE id = {0})
  AND ip.packetStatusId = 5
  ORDER BY id DESC
  LIMIT 1
  ;'''