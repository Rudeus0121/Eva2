from django.urls import path
from . import views_templates as vt

urlpatterns = [
    # Especialidades
    path('especialidades/', vt.listar_especialidades, name='listar_especialidades'),
    path('especialidades/nueva/', vt.crear_especialidad, name='crear_especialidad'),
    path('especialidades/editar/<int:pk>/', vt.editar_especialidad, name='editar_especialidad'),
    path('especialidades/eliminar/<int:pk>/', vt.eliminar_especialidad, name='eliminar_especialidad'),

    # Pacientes
    path('pacientes/', vt.listar_pacientes, name='listar_pacientes'),
    path('pacientes/nueva/', vt.crear_paciente, name='crear_paciente'),
    path('pacientes/editar/<int:pk>/', vt.editar_paciente, name='editar_paciente'),
    path('pacientes/eliminar/<int:pk>/', vt.eliminar_paciente, name='eliminar_paciente'),

    # Médicos
    path('medicos/', vt.listar_medicos, name='listar_medicos'),
    path('medicos/nueva/', vt.crear_medico, name='crear_medico'),
    path('medicos/editar/<int:pk>/', vt.editar_medico, name='editar_medico'),
    path('medicos/eliminar/<int:pk>/', vt.eliminar_medico, name='eliminar_medico'),

    # Consultas
    path('consultas/', vt.listar_consultas, name='listar_consultas'),
    path('consultas/nueva/', vt.crear_consulta, name='crear_consulta'),
    path('consultas/editar/<int:pk>/', vt.editar_consulta, name='editar_consulta'),
    path('consultas/eliminar/<int:pk>/', vt.eliminar_consulta, name='eliminar_consulta'),

    # Tratamientos
    path('tratamientos/', vt.listar_tratamientos, name='listar_tratamientos'),
    path('tratamientos/nueva/', vt.crear_tratamiento, name='crear_tratamiento'),
    path('tratamientos/editar/<int:pk>/', vt.editar_tratamiento, name='editar_tratamiento'),
    path('tratamientos/eliminar/<int:pk>/', vt.eliminar_tratamiento, name='eliminar_tratamiento'),

    # Medicamentos
    path('medicamentos/', vt.listar_medicamentos, name='listar_medicamentos'),
    path('medicamentos/nueva/', vt.crear_medicamento, name='crear_medicamento'),
    path('medicamentos/editar/<int:pk>/', vt.editar_medicamento, name='editar_medicamento'),
    path('medicamentos/eliminar/<int:pk>/', vt.eliminar_medicamento, name='eliminar_medicamento'),

    # Recetas
    path('recetas/', vt.listar_recetas, name='listar_recetas'),
    path('recetas/nueva/', vt.crear_receta, name='crear_receta'),
    path('recetas/editar/<int:pk>/', vt.editar_receta, name='editar_receta'),
    path('recetas/eliminar/<int:pk>/', vt.eliminar_receta, name='eliminar_receta'),
    path('', vt.home, name='home'),

]
