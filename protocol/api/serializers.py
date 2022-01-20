from django.db import models
from django.db.models import fields
from rest_framework import serializers
from ..models import Oosintegrationpacket, Oosintegrationpackettype
from django.db.models import Q


class IntegrationPacketSerializer(serializers.ModelSerializer):
    typeid = serializers.SerializerMethodField()
    class Meta:
        model = Oosintegrationpacket
        fields = '__all__'
   
    @staticmethod
    def get_typeid(obj):
        type_ = Oosintegrationpackettype.objects.using('sectionks').filter(id=obj.typeid.id).first() 
        return OosintegrationpackeTtypeSerializer(type_).data

class OosintegrationpackeTtypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oosintegrationpackettype
        fields = '__all__'
