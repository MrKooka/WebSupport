from django.urls import path
from rest_framework import routers
from .views import Test,Get44ekProcInfo,GetProcedureStatus
router = routers.SimpleRouter()
router.register('test', Test, basename='test')

urlpatterns =[
    path('test',Test.as_view()),
    path('',Get44ekProcInfo.as_view()),
    path('getProcedureStatus', GetProcedureStatus.as_view())
]
urlpatterns += router.urls  