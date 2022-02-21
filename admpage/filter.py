import django_filters
from .models import *


class workfilter(django_filters.FilterSet):
    class Meta:
        model = Worker
        fields = '__all__'


class sitefilter(django_filters.FilterSet):
    class Meta:
        model = Site
        fields = '__all__'
