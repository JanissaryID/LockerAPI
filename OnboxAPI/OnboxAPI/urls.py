
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views

from api.views import LockersList, LockersDetail

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/',include("api.urls")),
]