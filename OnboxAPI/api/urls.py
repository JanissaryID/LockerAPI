from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('',LockersList.as_view(), name = "list"),
    path('find',LockersDetail.as_view(), name = "FindID"),
    path('update/<str:IdLocker>/',LockersUpdate.as_view(), name = "UpdateID"),
    path('delete/<str:IdLocker>/',LockersDelete.as_view(), name = "DeleteID"),
    path('create',LockersCreate.as_view(), name = "CreateID"),

    # Box url views

    path('box',BoxList.as_view(), name = "FindBOX"),
    # path('box',BoxList.as_view(), name = "listbox"),
]