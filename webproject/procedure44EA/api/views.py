from pprint import pprint as pp
from django.db.models.query_utils import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Procedure44EAStatusSerializeer
from ..models import Procedurestatus





class Get44EAProcedureStatus(APIView):
    def get(self, request, format=None):
        statusList = Procedurestatus.objects.using('sectionks').all()
        return Response(Procedure44EAStatusSerializeer(statusList, many=True).data)
