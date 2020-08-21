from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('',LockersList.as_view(), name = "list"),
    path('find',LockersFind.as_view(), name = "FindID"),
    # path('update/<str:IdLocker>/',LockersUpdate.as_view(), name = "UpdateID"),
    # path('delete/<str:IdLocker>/',LockersDelete.as_view(), name = "DeleteID"),
]