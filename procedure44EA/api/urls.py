from django.urls import path
from rest_framework import routers
from .views import Get44EAProcedureStatus


router = routers.SimpleRouter()

urlpatterns =[
    path('get44EAProcedureStatus', Get44EAProcedureStatus.as_view())
]
urlpatterns += router.urls  