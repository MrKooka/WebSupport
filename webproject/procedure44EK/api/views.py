from pprint import pprint as pp
from django.db.models.query_utils import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProcSerializer,CatalogProcedureStatusSerializer
from ..models import Procedures,CatalogProcedureStatus
class Test(APIView):
    def get(self, request, format=None):
        if request.query_params['name']:
            print(request.query_params['name'])
        return Response({'name':'alex'})
    @classmethod
    def get_extra_actions(some):
        return []

class Get44ekProcInfo(APIView):

    def get(self, request, format=None):
        regNum = request.query_params.get('regNum',None)
        if regNum:
            procedure = Procedures.objects.filter(registrationnumber=regNum).first()
            return Response(ProcSerializer(procedure).data)
        return Response(None)



class GetProcedureStatus(APIView):
    def get(self, request, format=None):
        statusList = CatalogProcedureStatus.objects.using('catalog_44').all()
        return Response(CatalogProcedureStatusSerializer(statusList, many=True).data)