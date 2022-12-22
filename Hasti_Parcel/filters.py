import django_filters
from django_filters import DateFilter,CharFilter
from .models import *


    
class reportFilter(django_filters.FilterSet):
    
    class Meta:
        model=OP1
        fields = ['branch','city','companyName','description','description2','contractType','vehicle','status']


