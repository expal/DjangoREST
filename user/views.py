from django.contrib.admin import action
from rest_framework import generics, serializers, viewsets
from rest_framework.generics import UpdateAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Author, Project, TODO
from .serializers import AuthorModelSerializer
from .filters import ProjectFilter, TODOFilter


class AuthorViewSet(generics.ListAPIView, UpdateAPIView, RetrieveAPIView):
    queryset = Author.objects.all()
    renderer_classes = [JSONRenderer]
    serializer_class = AuthorModelSerializer


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectViewSet(generics.ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView,
                     viewsets.ModelViewSet):
    queryset = Project.objects.all()
    renderer_classes = [JSONRenderer]
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination
    filter_fields = ['name']
    filter_class = ProjectFilter


class TODOLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class TODOViewSet(generics.ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView,
                  viewsets.ModelViewSet):
    queryset = Project.objects.all()
    renderer_classes = [JSONRenderer]
    serializer_class = TODOModelSerializer
    pagination_class = TODOLimitOffsetPagination
    filter_fields = ['deleted']
    filter_class = TODOFilter
