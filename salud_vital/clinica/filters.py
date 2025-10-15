import django_filters
from .models import *

class MedicoFilter(django_filters.FilterSet):
    especialidad = django_filters.CharFilter(field_name='especialidad__nombre', lookup_expr='icontains')

    class Meta:
        model = Medico
        fields = ['especialidad']

class PacienteFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Paciente
        fields = ['nombre', 'rut']
