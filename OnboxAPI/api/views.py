from django.http import JsonResponse
from django.shortcuts import render

from rest_framework import mixins
from rest_framework import generics

from .models import Lockers
from .serializers import LockersSerializer

class LockersList(generics.ListCreateAPIView):
    queryset = Lockers.objects.all()
    serializer_class = LockersSerializer

class LockersDetail(generics.RetrieveAPIView):
    queryset = Lockers.objects.all()
    serializer_class = LockersSerializer
    lookup_field = 'IdLocker'

class LockersUpdate(generics.RetrieveUpdateAPIView):
    queryset = Lockers.objects.all()
    serializer_class = LockersSerializer
    lookup_field = 'IdLocker'

class LockersDelete(generics.RetrieveDestroyAPIView):
    queryset = Lockers.objects.all()
    serializer_class = LockersSerializer
    lookup_field = 'IdLocker'


# class LockersList(mixins.ListModelMixin,
#                     mixins.CreateModelMixin,
#                     generics.GenericAPIView):
#     queryset = Lockers.objects.all()
#     serializer_class = LockersSerializer
    
#     def get(self, request):
#         return JsonResponse(request)

#     # def get(self, request, *args, **kwargs):
#     #     return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class LockersDetail(mixins.RetrieveModelMixin,
#                     generics.GenericAPIView):
#     queryset = Lockers.objects.all()
#     serializer_class = LockersSerializer
#     lookup_field = 'IdLocker'

#     def get(self, request, IdLocker = None):
#         if IdLocker:
#             return self.retrieve(request, IdLocker)
#         else:
#             return self.list(request)

# class LockersUpdate(mixins.UpdateModelMixin,
#                     mixins.RetrieveModelMixin,
#                     generics.GenericAPIView):
#     queryset = Lockers.objects.all()
#     serializer_class = LockersSerializer
#     lookup_field = 'IdLocker'

#     def get(self, request, IdLocker = None):
#         if IdLocker:
#             return self.retrieve(request, IdLocker)
#         else:
#             return self.list(request)

#     def put(self, request, IdLocker = None):
#         return self.update(request, IdLocker)

# class LockersDelete(mixins.DestroyModelMixin,
#                     mixins.RetrieveModelMixin,
#                     generics.GenericAPIView):
#     queryset = Lockers.objects.all()
#     serializer_class = LockersSerializer
#     lookup_field = 'IdLocker'

#     def get(self, request, IdLocker = None):
#         if IdLocker:
#             return self.retrieve(request, IdLocker)
#         else:
#             return self.list(request)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)