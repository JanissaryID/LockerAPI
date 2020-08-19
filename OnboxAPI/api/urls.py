from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('',LockersList.as_view(), name = "list"),
    path('find/<str:IdLocker>/',LockersDetail.as_view(), name = "FindID"),
    path('update/<str:IdLocker>/',LockersUpdate.as_view(), name = "FindID"),
    path('delete/<str:IdLocker>/',LockersDelete.as_view(), name = "FindID"),
]