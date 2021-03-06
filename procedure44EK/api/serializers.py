from django.db import models
from django.db.models import fields
from rest_framework import serializers
from ..models import CatalogProcedureStatus, Procedures, Lot, Protocol, Request, Procedureevent


from django.db.models import Q

class ProcedureEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedureevent
        fields = [
            'id',
            'createdatetime',
            'typecode',
        ]


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = [
            'id',
            'createdatetime',
            'status'
        ]


class LotSerializer(serializers.ModelSerializer):
    protocol = serializers.SerializerMethodField()
    request = serializers.SerializerMethodField()

    class Meta:
        model = Lot
        fields = [
            'id',
            'status',
            'createdatetime',
            'protocol',
            'request'

        ]

    @staticmethod
    def get_protocol(obj):
        return ProtocolSerializer(Protocol.objects.filter(lotid=obj), many=True).data

    @staticmethod
    def get_request(obj):
        return RequestSerializer(Request.objects.filter(lotid=obj), many=True).data


class ProtocolSerializer(serializers.ModelSerializer):
    event = serializers.SerializerMethodField()

    class Meta:
        model = Protocol
        fields = [
            'id',
            'status',
            'editdatetime',
            'deleted_at',
            'event'
        ]

    @staticmethod
    def get_event(obj):
        protocolEventsAll = Procedureevent.objects.filter(protocolid=obj)
        events = protocolEventsAll.exclude(Q(typecode__contains='contract') & Q(typecode__contains='request.') & Q(typecode__contains='procedure.'))
        return ProcedureEventSerializer(events, many=True).data


class ProcSerializer(serializers.ModelSerializer):
    lot = serializers.SerializerMethodField()

    class Meta:
        model = Procedures
        fields = [
            'id',
            'registrationnumber',
            'status',
            'requestenddatetime',
            'requestreviewfirstpartsdatetime',
            'offerdate',
            'offerenddatetime',
            'requestreviewsecondpartsdatetime',
            'lot'
        ]
    @staticmethod
    def get_lot(obj):
        return LotSerializer(Lot.objects.filter(procedureid=obj).first()).data

        
class CatalogProcedureStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogProcedureStatus
        fields = '__all__'


