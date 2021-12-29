from django.db import models


class Oosintegrationpacket(models.Model):
    partnerfrom = models.CharField(db_column='partnerFrom', max_length=50)  # Field name made lowercase.
    partnerto = models.CharField(db_column='partnerTo', max_length=50)  # Field name made lowercase.
    guid = models.CharField(unique=True, max_length=100, blank=True, null=True)
    regnumber = models.CharField(db_column='regNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(max_length=50)
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    receivedatetime = models.DateTimeField(db_column='receiveDateTime', blank=True, null=True)  # Field name made lowercase.
    senddatetime = models.DateTimeField(db_column='sendDateTime', blank=True, null=True)  # Field name made lowercase.
    processdatetime = models.DateTimeField(db_column='processDateTime', blank=True, null=True)  # Field name made lowercase.
    contenturi = models.CharField(db_column='contentUri', max_length=255, blank=True, null=True)  # Field name made lowercase.
    indexnum = models.IntegerField(db_column='indexNum', blank=True, null=True)  # Field name made lowercase.
    sendingattempt = models.IntegerField(db_column='sendingAttempt', blank=True, null=True)  # Field name made lowercase.
    confirmationdatetime = models.DateTimeField(db_column='confirmationDateTime', blank=True, null=True)  # Field name made lowercase.
    confirmationresult = models.IntegerField(db_column='confirmationResult', blank=True, null=True)  # Field name made lowercase.
    externalreceiveddatetime = models.DateTimeField(db_column='externalReceivedDateTime', blank=True, null=True)  # Field name made lowercase.
    typeid = models.ForeignKey('Oosintegrationpackettype', models.DO_NOTHING, db_column='typeId')  # Field name made lowercase.
    packetstatusid = models.ForeignKey('Oosintegrationstatus', models.DO_NOTHING, db_column='packetStatusId')  # Field name made lowercase.
    confirmationid = models.ForeignKey('self', models.DO_NOTHING, db_column='confirmationId', blank=True, null=True)  # Field name made lowercase.
    packetid = models.IntegerField(db_column='packetId', blank=True, null=True)  # Field name made lowercase.
    objectid = models.TextField(db_column='objectId', blank=True, null=True)  # Field name made lowercase.
    archive = models.IntegerField(blank=True, null=True)
    params = models.TextField(blank=True, null=True)
    mode = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oosIntegrationPacket'

class Oosintegrationpackettype(models.Model):
    code = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    sendconfirmation = models.IntegerField(db_column='sendConfirmation', blank=True, null=True)  # Field name made lowercase.
    external = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oosIntegrationPacketType'


class Oosintegrationstatus(models.Model):
    code = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oosIntegrationStatus'