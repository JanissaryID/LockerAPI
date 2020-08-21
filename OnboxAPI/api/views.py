from django.http import JsonResponse
from django.shortcuts import render

from rest_framework import mixins
from rest_framework import generics

from .models import Lockers
from .serializers import LockersSerializer

from django_filters.rest_framework import DjangoFilterBackend

class LockersList(generics.ListCreateAPIView):
    queryset = Lockers.objects.all()
    serializer_class = LockersSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['IdLocker']

class LockersFind(generics.ListAPIView):
    queryset = Lockers.objects.all()
    serializer_class = LockersSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['IdLocker']

class LockersUpdate(generics.RetrieveUpdateAPIView):
    queryset = Lockers.objects.all()
    serializer_class = LockersSerializer
    lookup_field = 'IdLocker'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['IdLocker']

class LockersDelete(generics.RetrieveDestroyAPIView):
    queryset = Lockers.objects.all()
    serializer_class = LockersSerializer
    lookup_field = 'IdLocker'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['IdLocker']