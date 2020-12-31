import django_filters
from .models import *
from django_filters import CharFilter


class StudentFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    section = CharFilter(field_name='section', lookup_expr='icontains')

    class Meta:
        model = std_registration_form
        fields = [
            'name',
            'section',
        ]
