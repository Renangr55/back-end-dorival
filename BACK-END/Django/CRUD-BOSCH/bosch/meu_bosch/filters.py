import django_filters
from .models import Livro

class LivroFilter(django_filters.FilterSet):
    titulo = django_filters.CharFilter(lookup_expr='icontains')
    autor = django_filters.CharFilter(lookup_expr='icontains')
    ano = django_filters.NumberFilter()

    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'ano']
