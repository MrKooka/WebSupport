from django.db import models
from django.db.models import fields
from rest_framework import serializers
from ..models import Procedurestatus
from django.db.models import Q

class Procedure44EAStatusSerializeer(serializers.ModelSerializer):
    class Meta:
        model = Procedurestatus
        fields = '__all__'