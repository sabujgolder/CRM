import django_filters
from .models import *

class OrderFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(field_name='name',lookup_expr='icontains')
    class Meta:
        model = Order
        fields = '__all__'
