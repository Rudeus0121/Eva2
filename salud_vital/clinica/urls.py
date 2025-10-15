# clinica/urls.py
from rest_framework import routers
from django.urls import path, include
from .views import (
    EspecialidadViewSet,
    PacienteViewSet,
    MedicoViewSet,
    ConsultaMedicaViewSet,
    TratamientoViewSet,
    MedicamentoViewSet,
    RecetaMedicaViewSet,
)

router = routers.DefaultRouter()
router.register('especialidades', EspecialidadViewSet)
router.register('pacientes', PacienteViewSet)
router.register('medicos', MedicoViewSet)
router.register('consultas', ConsultaMedicaViewSet)
router.register('tratamientos', TratamientoViewSet)
router.register('medicamentos', MedicamentoViewSet)
router.register('recetas', RecetaMedicaViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Esto genera todos los endpoints automáticamente
]
