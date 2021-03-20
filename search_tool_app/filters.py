import django_filters
from .models import *


class PaperFilter(django_filters.FilterSet):

    class Meta:
        model = Paper
        fields = '__all__'
        exclude = ('pdf', 'date_added')
