from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import todoSerializers
from .models import ToDo

class Tasks(viewsets.ModelViewSet):
    queryset=ToDo.objects.all()
    serializer_class=todoSerializers