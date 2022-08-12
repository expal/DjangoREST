from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from .models import Project
from .serializers import ProjectModelSerializer


class AuthorModelViewSet(ModelViewSet):
    queryset = Project.objects.all()

    serializer_class = ProjectModelSerializer
