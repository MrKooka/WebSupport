from django.db import models

# 44ek
class Procedures(models.Model):
    # Field name made lowercase.
    createdatetime = models.DateTimeField(db_column='createDateTime')
    # Field name made lowercase.
    editdatetime = models.DateTimeField(
        db_column='editDateTime', blank=True, null=True)
    # Field name made lowercase.
    additionalinformation = models.CharField(
        db_column='additionalInformation', max_length=2000, blank=True, null=True)
    # Field name made lowercase.
    deliverysingle = models.CharField(
        db_column='deliverySingle', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    eisregistrationnumber = models.CharField(
        db_column='eisRegistrationNumber', max_length=255, blank=True, null=True)
    name = models.CharField(max_length=2000, blank=True, null=True)
    # Field name made lowercase.
    offerdate = models.DateTimeField(
        db_column='offerDate', blank=True, null=True)
    # Field name made lowercase.
    offerenddatetime = models.DateTimeField(
        db_column='offerEndDateTime', blank=True, null=True)
    # Field name made lowercase.
    placingway = models.CharField(
        db_column='placingWay', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    purchaseplace = models.CharField(
        db_column='purchasePlace', max_length=2000, blank=True, null=True)
    # Field name made lowercase.
    registrationnumber = models.CharField(
        db_column='registrationNumber', max_length=256, blank=True, null=True)
    # Field name made lowercase.
    requestenddatetime = models.DateTimeField(
        db_column='requestEndDateTime', blank=True, null=True)
    requestreviewfirstpartsdatetime = models.DateTimeField(
        db_column='requestReviewFirstPartsDateTime', blank=True, null=True)  # Field name made lowercase.
    specializedorganizationid = models.IntegerField(
        db_column='specializedOrganizationId', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    customerid = models.IntegerField(db_column='customerId')
    status = models.CharField(max_length=255, blank=True, null=True)
    # Field name made lowercase.
    tradeurl = models.CharField(
        db_column='tradeUrl', max_length=2000, blank=True, null=True)
    # Field name made lowercase.
    publicationdatetime = models.DateTimeField(
        db_column='publicationDateTime', blank=True, null=True)
    # Field name made lowercase.
    guaranteefee = models.DecimalField(
        db_column='guaranteeFee', max_digits=22, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    guaranteefeepercent = models.DecimalField(
        db_column='guaranteeFeePercent', max_digits=5, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    customerpostaladdress = models.CharField(
        db_column='customerPostalAddress', max_length=2000, blank=True, null=True)
    # Field name made lowercase.
    changedescription = models.CharField(
        db_column='changeDescription', max_length=2000, blank=True, null=True)
    # Field name made lowercase.
    isaffliction = models.IntegerField(
        db_column='isAffliction', blank=True, null=True)
    isnotunscrupuloussuppliers = models.IntegerField(
        db_column='isNotUnscrupulousSuppliers', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    archive = models.IntegerField(blank=True, null=True)
    guid = models.CharField(max_length=255, blank=True, null=True)
    # Field name made lowercase.
    actualid = models.ForeignKey(
        'self', models.DO_NOTHING, db_column='actualId', blank=True, null=True)
    # Field name made lowercase.
    contactid = models.ForeignKey(
        'Contact', models.DO_NOTHING, db_column='contactId')
    # Field name made lowercase.
    signatureid = models.ForeignKey(
        'Signature', models.DO_NOTHING, db_column='signatureId', blank=True, null=True)
    discriminator = models.CharField(max_length=255)
    # Field name made lowercase.
    printform = models.CharField(
        db_column='printForm', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    eishref = models.CharField(
        db_column='eisHref', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    requestorder = models.CharField(
        db_column='requestOrder', max_length=2000, blank=True, null=True)
    # Field name made lowercase.
    contracttermadd = models.CharField(
        db_column='contractTermAdd', max_length=2000, blank=True, null=True)
    # Field name made lowercase.
    contractconditionsadd = models.CharField(
        db_column='contractConditionsAdd', max_length=2000, blank=True, null=True)
    requestreviewsecondpartsdatetime = models.DateTimeField(
        db_column='requestReviewSecondPartsDateTime', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    mustpublicdiscussion = models.IntegerField(
        db_column='mustPublicDiscussion', blank=True, null=True)
    # Field name made lowercase.
    flowerror = models.IntegerField(
        db_column='flowError', blank=True, null=True)
    # Field name made lowercase.
    modificationid = models.ForeignKey(
        'Proceduremodification', models.DO_NOTHING, db_column='modificationId', blank=True, null=True)
    publicdiscussionid = models.ForeignKey('Procedurepublicdiscussion', models.DO_NOTHING,
                                           db_column='publicDiscussionId', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    contractserviceinfo = models.TextField(
        db_column='contractServiceInfo', blank=True, null=True)
    requestprocessedenddatetime = models.DateTimeField(
        db_column='requestProcessedEndDateTime', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    externalid = models.CharField(
        db_column='externalId', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    responsiblerole = models.CharField(
        db_column='responsibleRole', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    regulateddatetime = models.DateTimeField(
        db_column='regulatedDateTime', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procedures'


class Contact(models.Model):
    # Field name made lowercase.
    firstname = models.CharField(
        db_column='firstName', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    lastname = models.CharField(
        db_column='lastName', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    middlename = models.CharField(
        db_column='middleName', max_length=300, blank=True, null=True)
    email = models.CharField(max_length=300, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    fax = models.CharField(max_length=30, blank=True, null=True)
    # Field name made lowercase.
    additionalinformation = models.CharField(
        db_column='additionalInformation', max_length=2000, blank=True, null=True)
    discriminator = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'contact'


class Signature(models.Model):
    # Field name made lowercase.
    createdatetime = models.DateTimeField(db_column='createDateTime')
    # Field name made lowercase.
    userid = models.IntegerField(db_column='userId', blank=True, null=True)
    # Field name made lowercase.
    certificateserial = models.TextField(
        db_column='certificateSerial', blank=True, null=True)
    # Field name made lowercase.
    certificateissuer = models.TextField(
        db_column='certificateIssuer', blank=True, null=True)
    # Field name made lowercase.
    certificateperson = models.TextField(
        db_column='certificatePerson', blank=True, null=True)
    # Field name made lowercase.
    signingdatetime = models.DateTimeField(
        db_column='signingDateTime', blank=True, null=True)
    # Field name made lowercase.
    stringdatauri = models.CharField(
        db_column='stringDataUri', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    signeddatauri = models.CharField(
        db_column='signedDataUri', max_length=255, blank=True, null=True)
    encoding = models.CharField(max_length=255, blank=True, null=True)
    # Field name made lowercase.
    enhancedsigneddatauri = models.CharField(
        db_column='enhancedSignedDataUri', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    isenhanced = models.IntegerField(
        db_column='isEnhanced', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'signature'


class Proceduremodification(models.Model):
    info = models.CharField(max_length=2000, blank=True, null=True)
    # Field name made lowercase.
    addinfo = models.CharField(
        db_column='addInfo', max_length=2000, blank=True, null=True)
    # Field name made lowercase.
    changereasonid = models.OneToOneField(
        'Procedurechangereason', models.DO_NOTHING, db_column='changeReasonId', blank=True, null=True, related_name='Prcdurchngrsn')

    class Meta:
        managed = False
        db_table = 'procedureModification'


class Procedurepublicdiscussion(models.Model):
    # Field name made lowercase.
    createdatetime = models.DateTimeField(db_column='createDateTime')
    number = models.CharField(max_length=12, blank=True, null=True)
    # Field name made lowercase.
    organizationch5st15 = models.IntegerField(
        db_column='organizationCh5St15', blank=True, null=True)
    href = models.CharField(max_length=1024, blank=True, null=True)
    # Field name made lowercase.
    protocoldate = models.DateTimeField(
        db_column='protocolDate', blank=True, null=True)
    # Field name made lowercase.
    protocolpublishdate = models.DateTimeField(
        db_column='protocolPublishDate', blank=True, null=True)
    # Field name made lowercase.
    publicdiscussionphase2num = models.CharField(
        db_column='publicDiscussionPhase2Num', max_length=12, blank=True, null=True)
    # Field name made lowercase.
    hrefphase2 = models.CharField(
        db_column='hrefPhase2', max_length=1024, blank=True, null=True)
    place = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procedurePublicDiscussion'


class Lot(models.Model):
    # Field name made lowercase.
    additioninfo = models.CharField(
        db_column='additionInfo', max_length=2000, blank=True, null=True)
    # Field name made lowercase.
    combinepurchase = models.IntegerField(db_column='combinePurchase')
    # Field name made lowercase.
    currencycode = models.CharField(
        db_column='currencyCode', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    defaultcontractnumber = models.CharField(
        db_column='defaultContractNumber', max_length=16, blank=True, null=True)
    # Field name made lowercase.
    deliverysingle = models.CharField(
        db_column='deliverySingle', max_length=255, blank=True, null=True)
    name = models.CharField(max_length=2000, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=40, blank=True, null=True)
    # Field name made lowercase.
    maxsum = models.DecimalField(
        db_column='maxSum', max_digits=22, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    impossibledetermine = models.IntegerField(
        db_column='impossibleDetermine', blank=True, null=True)
    # Field name made lowercase.
    commonsumspareparts = models.DecimalField(
        db_column='commonSumSpareParts', max_digits=22, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    commonamountrequest = models.CharField(
        db_column='commonAmountRequest', max_length=40, blank=True, null=True)
    schedule = models.CharField(max_length=2000, blank=True, null=True)
    contractwithseveralmembers = models.IntegerField(
        db_column='contractWithSeveralMembers', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    countmembers = models.IntegerField(
        db_column='countMembers', blank=True, null=True)
    # Field name made lowercase.
    createdatetime = models.DateTimeField(
        db_column='createDateTime', blank=True, null=True)
    # Field name made lowercase.
    editdatetime = models.DateTimeField(
        db_column='editDateTime', blank=True, null=True)
    cancelled = models.IntegerField()
    # Field name made lowercase.
    cancelleddatetime = models.DateTimeField(
        db_column='cancelledDateTime', blank=True, null=True)
    # Field name made lowercase.
    endtradedatetime = models.DateTimeField(
        db_column='endTradeDateTime', blank=True, null=True)
    # Field name made lowercase.
    tradeduration = models.CharField(
        db_column='tradeDuration', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    startpricefall = models.DecimalField(
        db_column='startPriceFall', max_digits=10, decimal_places=2, blank=True, null=True)
    observers = models.TextField(blank=True, null=True)
    # Field name made lowercase.
    externalguid = models.CharField(
        db_column='externalGuid', max_length=36, blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    archive = models.IntegerField(blank=True, null=True)
    guid = models.CharField(max_length=255, blank=True, null=True)
    # Field name made lowercase.
    actualid = models.ForeignKey(
        'self', models.DO_NOTHING, db_column='actualId', blank=True, null=True)
    # Field name made lowercase.
    procedureid = models.ForeignKey(
        'Procedures', models.DO_NOTHING, db_column='procedureId')
    discriminator = models.CharField(max_length=255)
    # Field name made lowercase.
    isdrugs = models.IntegerField(db_column='isDrugs', blank=True, null=True)
    # Field name made lowercase.
    flowerror = models.IntegerField(
        db_column='flowError', blank=True, null=True)
    # Field name made lowercase.
    documentationid = models.ForeignKey(
        'Lotdocumentation', models.DO_NOTHING, db_column='documentationId', blank=True, null=True)
    # Field name made lowercase.
    totalsum = models.CharField(
        db_column='totalSum', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    externalid = models.CharField(
        db_column='externalId', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    iscontractblocked = models.IntegerField(
        db_column='isContractBlocked', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lot'


class Lotdocumentation(models.Model):
    # Field name made lowercase.
    contractmultiinfo = models.IntegerField(
        db_column='contractMultiInfo', blank=True, null=True)
    # Field name made lowercase.
    contractcount = models.IntegerField(
        db_column='contractCount', blank=True, null=True)
    # Field name made lowercase.
    purchaseobjectsch9st37 = models.IntegerField(
        db_column='purchaseObjectsCh9St37', blank=True, null=True)
    modifiable = models.IntegerField(blank=True, null=True)
    research = models.IntegerField(blank=True, null=True)
    # Field name made lowercase.
    printform = models.CharField(
        db_column='printForm', max_length=255, blank=True, null=True)
    discriminator = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'lotDocumentation'


class Protocol(models.Model):
    protocol_commission = models.ForeignKey(
        'ProtocolCommission', models.DO_NOTHING, blank=True, null=True)
    # Field name made lowercase.
    createdatetime = models.DateTimeField(db_column='createDateTime')
    # Field name made lowercase.
    editdatetime = models.DateTimeField(
        db_column='editDateTime', blank=True, null=True)
    # Field name made lowercase.
    publishdatetime = models.DateTimeField(
        db_column='publishDateTime', blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    guid = models.CharField(max_length=255, blank=True, null=True)
    # Field name made lowercase.
    lotid = models.ForeignKey('Lot', models.DO_NOTHING,
                              db_column='lotId', blank=True, null=True)
    # Field name made lowercase.
    signatureid = models.ForeignKey(
        'Signature', models.DO_NOTHING, db_column='signatureId', blank=True, null=True)
    discriminator = models.CharField(max_length=255)
    # Field name made lowercase.
    additionalinfo = models.CharField(
        db_column='additionalInfo', max_length=2000, blank=True, null=True)
    # Field name made lowercase.
    withmultipleparticipants = models.IntegerField(
        db_column='withMultipleParticipants', blank=True, null=True)
    # Field name made lowercase.
    documentid = models.ForeignKey(
        'Protocoldocuments', models.DO_NOTHING, db_column='documentId', blank=True, null=True)
    # Field name made lowercase.
    abandonedreason = models.CharField(
        db_column='abandonedReason', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    afterprolongation = models.IntegerField(
        db_column='afterProlongation', blank=True, null=True)
    # Field name made lowercase.
    isevaluated = models.IntegerField(
        db_column='isEvaluated', blank=True, null=True)
    # Field name made lowercase.
    applicationid = models.ForeignKey(
        'Protocoldocuments', models.DO_NOTHING, db_column='applicationId', blank=True, null=True, related_name='applId')
    # Field name made lowercase.
    operatorsignatureid = models.ForeignKey(
        'Signature', models.DO_NOTHING, db_column='operatorSignatureId', blank=True, null=True,related_name='operatSign')
    # Field name made lowercase.
    issinglepart = models.IntegerField(
        db_column='isSinglePart', blank=True, null=True)
    cancelled = models.IntegerField(blank=True, null=True)
    # Field name made lowercase.
    seconddocumentid = models.ForeignKey(
        'Protocoldocuments', models.DO_NOTHING, db_column='secondDocumentId', blank=True, null=True, related_name='document')
    # Field name made lowercase.
    proceduredate = models.DateTimeField(
        db_column='procedureDate', blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    external_id = models.CharField(max_length=64, blank=True, null=True)
    # Field name made lowercase.
    protocoltype = models.CharField(
        db_column='protocolType', max_length=50, blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    archive = models.IntegerField(blank=True, null=True)
    # Field name made lowercase.
    actualid = models.ForeignKey(
        'self', models.DO_NOTHING, db_column='actualId', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'protocol'

class Request(models.Model):
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    editdatetime = models.DateTimeField(db_column='editDateTime', blank=True, null=True)  # Field name made lowercase.
    number = models.IntegerField(blank=True, null=True)
    goodspricetype = models.CharField(db_column='goodsPriceType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lotversion = models.IntegerField(db_column='lotVersion', blank=True, null=True)  # Field name made lowercase.
    procedureversion = models.IntegerField(db_column='procedureVersion', blank=True, null=True)  # Field name made lowercase.
    publicationdatetime = models.DateTimeField(db_column='publicationDateTime', blank=True, null=True)  # Field name made lowercase.
    refuseddatetime = models.DateTimeField(db_column='refusedDateTime', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=255, blank=True, null=True)
    supplierid = models.IntegerField(db_column='supplierId')  # Field name made lowercase.
    memberid = models.IntegerField(db_column='memberId', blank=True, null=True)  # Field name made lowercase.
    supplierpassportdata = models.CharField(db_column='supplierPassportData', max_length=255, blank=True, null=True)  # Field name made lowercase.
    supplieremail = models.CharField(db_column='supplierEmail', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tradeposition = models.IntegerField(db_column='tradePosition', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    archive = models.IntegerField(blank=True, null=True)
    guid = models.CharField(max_length=255, blank=True, null=True)
    actualid = models.ForeignKey('self', models.DO_NOTHING, db_column='actualId', blank=True, null=True)  # Field name made lowercase.
    contactid = models.ForeignKey('Contact', models.DO_NOTHING, db_column='contactId')  # Field name made lowercase.
    contractfinalofferid = models.ForeignKey('Offer', models.DO_NOTHING, db_column='contractFinalOfferId', blank=True, null=True,related_name='contractFinalOff')  # Field name made lowercase.
    contractofferid = models.ForeignKey('Offer', models.DO_NOTHING, db_column='contractOfferId', blank=True, null=True)  # Field name made lowercase.
    lotid = models.ForeignKey('Lot', models.DO_NOTHING, db_column='lotId')  # Field name made lowercase.
    signatureid = models.ForeignKey('Signature', models.DO_NOTHING, db_column='signatureId', blank=True, null=True,related_name='signn')  # Field name made lowercase.
    refusedsignatureid = models.ForeignKey('Signature', models.DO_NOTHING, db_column='refusedSignatureId', blank=True, null=True, related_name='rfsdSign')  # Field name made lowercase.
    discriminator = models.CharField(max_length=255)
    agreement = models.IntegerField(blank=True, null=True)
    afterprolongation = models.IntegerField(db_column='afterProlongation', blank=True, null=True)  # Field name made lowercase.
    flowerror = models.IntegerField(db_column='flowError', blank=True, null=True)  # Field name made lowercase.
    partssignatureid = models.ForeignKey('Signature', models.DO_NOTHING, db_column='partsSignatureId', blank=True, null=True,related_name='prtsSign')  # Field name made lowercase.
    firstpartsignatureid = models.ForeignKey('Signature', models.DO_NOTHING, db_column='firstPartSignatureId', blank=True, null=True,related_name='frstPrtsSign')  # Field name made lowercase.
    secondpartsignatureid = models.ForeignKey('Signature', models.DO_NOTHING, db_column='secondPartSignatureId', blank=True, null=True, related_name='secondprtSign')  # Field name made lowercase.
    specaccount_accountnumber = models.CharField(db_column='specAccount_accountNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    specaccount_id = models.IntegerField(db_column='specAccount_id', blank=True, null=True)  # Field name made lowercase.
    specaccount_bankname = models.CharField(db_column='specAccount_bankName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    specaccount_bankcode = models.CharField(db_column='specAccount_bankCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    specaccount_obligationtooperator = models.IntegerField(db_column='specAccount_obligationToOperator', blank=True, null=True)  # Field name made lowercase.
    publicinstitution = models.IntegerField(db_column='publicInstitution', blank=True, null=True)  # Field name made lowercase.
    specaccount_clienttype = models.IntegerField(db_column='specAccount_clientType', blank=True, null=True)  # Field name made lowercase.
    specaccount_name = models.CharField(db_column='specAccount_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    specaccount_inn = models.CharField(db_column='specAccount_inn', max_length=255, blank=True, null=True)  # Field name made lowercase.
    specaccount_kpp = models.CharField(db_column='specAccount_kpp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    specaccount_ogrn = models.CharField(db_column='specAccount_ogrn', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bankguarantee = models.CharField(db_column='bankGuarantee', max_length=20, blank=True, null=True)  # Field name made lowercase.
    specaccount_bankguarantee = models.IntegerField(db_column='specAccount_bankGuarantee', blank=True, null=True)  # Field name made lowercase.
    additionalinfo = models.TextField(db_column='additionalInfo', blank=True, null=True)  # Field name made lowercase.
    firstpartoperatorsignatureid = models.ForeignKey('Signature', models.DO_NOTHING, db_column='firstPartOperatorSignatureId', blank=True, null=True)  # Field name made lowercase.
    secondpartoperatorsignatureid = models.ForeignKey('Signature', models.DO_NOTHING, db_column='secondPartOperatorSignatureId', blank=True, null=True, related_name='scndPrtOperSing')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='ipAddress', max_length=16, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'request'

class Offer(models.Model):
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    editdatetime = models.DateTimeField(db_column='editDateTime', blank=True, null=True)  # Field name made lowercase.
    publishdatetime = models.DateTimeField(db_column='publishDateTime', blank=True, null=True)  # Field name made lowercase.
    value = models.DecimalField(max_digits=31, decimal_places=11, blank=True, null=True)
    discriminator = models.CharField(max_length=255)
    iscontest = models.IntegerField(db_column='isContest', blank=True, null=True)  # Field name made lowercase.
    offersignatureid = models.ForeignKey('Signature', models.DO_NOTHING, db_column='offerSignatureId', blank=True, null=True, related_name='orftSigtId')  # Field name made lowercase.
    offeroperatorsignatureid = models.ForeignKey('Signature', models.DO_NOTHING, db_column='offerOperatorSignatureId', blank=True, null=True, related_name='ofrOprSignId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'offer'


class Protocoldocuments(models.Model):
    title = models.CharField(max_length=2000, blank=True, null=True)
    realname = models.CharField(db_column='realName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    uri = models.CharField(max_length=255, blank=True, null=True)
    hash = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'protocolDocuments'


class ProtocolCommission(models.Model):
    date_update = models.DateTimeField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    commission_id = models.IntegerField(blank=True, null=True)
    decision_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'protocol_commission'


class Procedureevent(models.Model):
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    editdatetime = models.DateTimeField(db_column='editDateTime', blank=True, null=True)  # Field name made lowercase.
    publicationdatetime = models.DateTimeField(db_column='publicationDateTime', blank=True, null=True)  # Field name made lowercase.
    params = models.TextField(blank=True, null=True)
    discriminator = models.CharField(max_length=255)
    typecode = models.CharField(db_column='typeCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    link = models.CharField(max_length=255, blank=True, null=True)
    guid = models.CharField(max_length=255, blank=True, null=True)
    procedureid = models.ForeignKey('Procedures', models.DO_NOTHING, db_column='procedureId', blank=True, null=True)  # Field name made lowercase.
    lotid = models.ForeignKey('Lot', models.DO_NOTHING, db_column='lotId', blank=True, null=True)  # Field name made lowercase.
    protocolid = models.ForeignKey('Protocol', models.DO_NOTHING, db_column='protocolId', blank=True, null=True)  # Field name made lowercase.
    requestid = models.ForeignKey('Request', models.DO_NOTHING, db_column='requestId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'procedureEvent'


class Procedurechangereason(models.Model):
    discriminator = models.CharField(max_length=255)
    checkresultnumber = models.CharField(db_column='checkResultNumber', max_length=256, blank=True, null=True)  # Field name made lowercase.
    prescriptionnumber = models.CharField(db_column='prescriptionNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    foundation = models.CharField(max_length=2000, blank=True, null=True)
    authorityname = models.CharField(db_column='authorityName', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    authoritytype = models.CharField(db_column='authorityType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    docname = models.CharField(db_column='docName', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    docnumber = models.CharField(db_column='docNumber', max_length=350, blank=True, null=True)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='docDate', blank=True, null=True)  # Field name made lowercase.
    courtname = models.CharField(db_column='courtName', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    decisiondate = models.DateTimeField(db_column='decisionDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'procedureChangeReason'

class CatalogProcedureStatus(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'catalog_procedure_status'
        unique_together = (('code', 'type'),)

        
class EDORouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        if model._meta.app_label == 'edo':
            return 'edo'
        elif model._meta.app_label == 'procedure44EK':
            return '44ek'
        return None


