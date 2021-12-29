from pprint import pprint as pp
from django.db.models.query_utils import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from .serializers import IntegrationPacketSerializer, OosintegrationpackeTtypeSerializer
from ..models import Oosintegrationpacket, Oosintegrationpackettype

class GetProtocol(APIView):
    def get(self, request, format=None):
        regNum = request.query_params.get('regNum', None)
        if regNum:
            query = (Oosintegrationpacket.objects
                     .using('sectionks')
                     .filter(
                         regnumber=regNum,
                         typeid__in=settings.PROTOCOL_PROCEDURES,
                         packetstatusid=5,
                         confirmationresult=1)
                     .select_related('typeid')
                     .all())

            return Response(IntegrationPacketSerializer(query, many=True).data)
        return Response({'text':'regNum not found'})

    @classmethod
    def get_extra_actions(some):
        return []
