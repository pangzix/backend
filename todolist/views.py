from django.shortcuts import render
from rest_framework import viewsets,mixins
from .serializers import TodoSerializer
from .models import TodoList


class TodolistViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer
