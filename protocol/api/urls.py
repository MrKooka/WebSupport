from django.urls import path
from rest_framework import routers
from .views import GetProtocol


router = routers.SimpleRouter()

urlpatterns =[
    path('getprotocol', GetProtocol.as_view())
]
urlpatterns += router.urls  