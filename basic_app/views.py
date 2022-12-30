from django.shortcuts import render
from rest_framework import generics

from basic_app import serializers, models


#


class ListUser(generics.ListCreateAPIView):
    queryset = models.Link.objects.all()
    serializer_class = serializers.UserSerializer



class DeatilUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Link.objects.all()
    serializer_class = serializers.UserSerializer

