from django_filters import rest_framework as filters


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name']


class TODOFilter(filters.FilterSet):
    deleted = filters.BooleanFilter(lookup_expr='true')

    class Meta:
        model = TODO
        fields = ['deleted']
