from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *

# -------------------- ESPECIALIDAD --------------------
class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'descripcion']


# -------------------- PACIENTE --------------------
class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # ✅ Puedes filtrar pacientes por su estado activo
    filterset_fields = ['activo']
    # ✅ También puedes buscarlos por nombre, apellido o RUT
    search_fields = ['nombre', 'apellido', 'rut']


# -------------------- MÉDICO --------------------
class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # ✅ Filtrar médicos por especialidad
    filterset_fields = ['especialidad', 'activo']
    # ✅ Buscar por nombre, apellido o rut
    search_fields = ['nombre', 'apellido', 'rut']


# -------------------- CONSULTA MÉDICA --------------------
class ConsultaMedicaViewSet(viewsets.ModelViewSet):
    queryset = ConsultaMedica.objects.all()
    serializer_class = ConsultaMedicaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # ✅ Filtrar consultas por médico, paciente o estado
    filterset_fields = ['medico', 'paciente', 'estado']
    # ✅ Buscar por motivo o diagnóstico
    search_fields = ['motivo', 'diagnostico']


# -------------------- TRATAMIENTO --------------------
class TratamientoViewSet(viewsets.ModelViewSet):
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # ✅ Filtrar tratamientos por consulta
    filterset_fields = ['consulta']
    search_fields = ['descripcion', 'observaciones']


# -------------------- MEDICAMENTO --------------------
class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # ✅ Filtrar medicamentos por laboratorio o stock
    filterset_fields = ['laboratorio']
    search_fields = ['nombre', 'laboratorio']


# -------------------- RECETA MÉDICA --------------------
class RecetaMedicaViewSet(viewsets.ModelViewSet):
    queryset = RecetaMedica.objects.all()
    serializer_class = RecetaMedicaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # ✅ Filtrar recetas por tratamiento o medicamento
    filterset_fields = ['tratamiento', 'medicamento']
    search_fields = ['dosis', 'frecuencia', 'duracion']
