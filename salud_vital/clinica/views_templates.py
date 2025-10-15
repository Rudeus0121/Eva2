from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    Especialidad, Paciente, Medico,
    ConsultaMedica, Tratamiento,
    Medicamento, RecetaMedica
)
from .forms import (
    EspecialidadForm, PacienteForm, MedicoForm,
    ConsultaMedicaForm, TratamientoForm,
    MedicamentoForm, RecetaMedicaForm
)

# ------------------- ESPECIALIDADES -------------------
def listar_especialidades(request):
    especialidades = Especialidad.objects.all()
    return render(request, 'especialidad/lista.html', {'especialidades': especialidades})

def crear_especialidad(request):
    if request.method == 'POST':
        form = EspecialidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_especialidades')
    else:
        form = EspecialidadForm()
    return render(request, 'especialidad/form.html', {'form': form, 'accion': 'Crear'})

def editar_especialidad(request, pk):
    especialidad = get_object_or_404(Especialidad, pk=pk)
    if request.method == 'POST':
        form = EspecialidadForm(request.POST, instance=especialidad)
        if form.is_valid():
            form.save()
            return redirect('listar_especialidades')
    else:
        form = EspecialidadForm(instance=especialidad)
    return render(request, 'especialidad/form.html', {'form': form, 'accion': 'Editar'})

def eliminar_especialidad(request, pk):
    especialidad = get_object_or_404(Especialidad, pk=pk)
    if request.method == 'POST':
        especialidad.delete()
        return redirect('listar_especialidades')
    return render(request, 'especialidad/confirmar_eliminar.html', {'obj': especialidad})


# ------------------- PACIENTES -------------------
def listar_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'paciente/lista.html', {'pacientes': pacientes})

def crear_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'paciente/form.html', {'form': form, 'accion': 'Crear'})

def editar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('listar_pacientes')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'paciente/form.html', {'form': form, 'accion': 'Editar'})

def eliminar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        paciente.delete()
        return redirect('listar_pacientes')
    return render(request, 'paciente/confirmar_eliminar.html', {'obj': paciente})


# ------------------- MÉDICOS -------------------
def listar_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'medico/lista.html', {'medicos': medicos})

def crear_medico(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_medicos')
    else:
        form = MedicoForm()
    return render(request, 'medico/form.html', {'form': form, 'accion': 'Crear'})

def editar_medico(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    if request.method == 'POST':
        form = MedicoForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            return redirect('listar_medicos')
    else:
        form = MedicoForm(instance=medico)
    return render(request, 'medico/form.html', {'form': form, 'accion': 'Editar'})

def eliminar_medico(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    if request.method == 'POST':
        medico.delete()
        return redirect('listar_medicos')
    return render(request, 'medico/confirmar_eliminar.html', {'obj': medico})


# ------------------- CONSULTAS -------------------
def listar_consultas(request):
    consultas = ConsultaMedica.objects.all()
    return render(request, 'consulta_medica/lista.html', {'consultas': consultas})

def crear_consulta(request):
    if request.method == 'POST':
        form = ConsultaMedicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_consultas')
    else:
        form = ConsultaMedicaForm()
    return render(request, 'consulta_medica/form.html', {'form': form, 'accion': 'Crear'})

def editar_consulta(request, pk):
    consulta = get_object_or_404(ConsultaMedica, pk=pk)
    if request.method == 'POST':
        form = ConsultaMedicaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('listar_consultas')
    else:
        form = ConsultaMedicaForm(instance=consulta)
    return render(request, 'consulta_medica/form.html', {'form': form, 'accion': 'Editar'})

def eliminar_consulta(request, pk):
    consulta = get_object_or_404(ConsultaMedica, pk=pk)
    if request.method == 'POST':
        consulta.delete()
        return redirect('listar_consultas')
    return render(request, 'consulta_medica/confirmar_eliminar.html', {'obj': consulta})


# ------------------- TRATAMIENTOS -------------------
def listar_tratamientos(request):
    tratamientos = Tratamiento.objects.all()
    return render(request, 'tratamiento/lista.html', {'tratamientos': tratamientos})

def crear_tratamiento(request):
    if request.method == 'POST':
        form = TratamientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tratamientos')
    else:
        form = TratamientoForm()
    return render(request, 'tratamiento/form.html', {'form': form, 'accion': 'Crear'})

def editar_tratamiento(request, pk):
    tratamiento = get_object_or_404(Tratamiento, pk=pk)
    if request.method == 'POST':
        form = TratamientoForm(request.POST, instance=tratamiento)
        if form.is_valid():
            form.save()
            return redirect('listar_tratamientos')
    else:
        form = TratamientoForm(instance=tratamiento)
    return render(request, 'tratamiento/form.html', {'form': form, 'accion': 'Editar'})

def eliminar_tratamiento(request, pk):
    tratamiento = get_object_or_404(Tratamiento, pk=pk)
    if request.method == 'POST':
        tratamiento.delete()
        return redirect('listar_tratamientos')
    return render(request, 'tratamiento/confirmar_eliminar.html', {'obj': tratamiento})


# ------------------- MEDICAMENTOS -------------------
def listar_medicamentos(request):
    medicamentos = Medicamento.objects.all()
    return render(request, 'medicamento/lista.html', {'medicamentos': medicamentos})

def crear_medicamento(request):
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_medicamentos')
    else:
        form = MedicamentoForm()
    return render(request, 'medicamento/form.html', {'form': form, 'accion': 'Crear'})

def editar_medicamento(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    if request.method == 'POST':
        form = MedicamentoForm(request.POST, instance=medicamento)
        if form.is_valid():
            form.save()
            return redirect('listar_medicamentos')
    else:
        form = MedicamentoForm(instance=medicamento)
    return render(request, 'medicamento/form.html', {'form': form, 'accion': 'Editar'})

def eliminar_medicamento(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    if request.method == 'POST':
        medicamento.delete()
        return redirect('listar_medicamentos')
    return render(request, 'medicamento/confirmar_eliminar.html', {'obj': medicamento})


# ------------------- RECETAS -------------------
def listar_recetas(request):
    recetas = RecetaMedica.objects.all()
    return render(request, 'receta_medica/lista.html', {'recetas': recetas})

def crear_receta(request):
    if request.method == 'POST':
        form = RecetaMedicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_recetas')
    else:
        form = RecetaMedicaForm()
    return render(request, 'receta_medica/form.html', {'form': form, 'accion': 'Crear'})

def editar_receta(request, pk):
    receta = get_object_or_404(RecetaMedica, pk=pk)
    if request.method == 'POST':
        form = RecetaMedicaForm(request.POST, instance=receta)
        if form.is_valid():
            form.save()
            return redirect('listar_recetas')
    else:
        form = RecetaMedicaForm(instance=receta)
    return render(request, 'receta_medica/form.html', {'form': form, 'accion': 'Editar'})

def eliminar_receta(request, pk):
    receta = get_object_or_404(RecetaMedica, pk=pk)
    if request.method == 'POST':
        receta.delete()
        return redirect('listar_recetas')
def home(request):
    return render(request, 'home.html')
