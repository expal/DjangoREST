from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Author


class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author

        fields = '__all__'


class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project

        fields = '__all__'


class TODOModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TODO

        fields = '__all__'