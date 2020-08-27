from django.http import JsonResponse
from django.shortcuts import render

from rest_framework import mixins
from rest_framework import generics

from .models import Lockers, Boxs
from .serializers import LockersSerializer, BoxSerializer

from django_filters.rest_framework import DjangoFilterBackend

class LockersList(generics.ListCreateAPIView):
    queryset = Lockers.objects.all()
    serializer_class = LockersSerializer

class LockersDetail(generics.ListAPIView):
    queryset = Lockers.objects.all()
    serializer_class = LockersSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['IdLocker']

class LockersCreate(generics.CreateAPIView):
    queryset = Lockers.objects.all()
    serializer_class = LockersSerializer

class LockersUpdate(generics.RetrieveUpdateAPIView):
    queryset = Lockers.objects.all()
    serializer_class = LockersSerializer
    lookup_field = 'IdLocker'

class LockersDelete(generics.RetrieveDestroyAPIView):
    queryset = Lockers.objects.all()
    serializer_class = LockersSerializer
    lookup_field = 'IdLocker'

# Box Views Class

class BoxList(generics.ListCreateAPIView):
    queryset = Boxs.objects.all()
    serializer_class = BoxSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['IdLocker']