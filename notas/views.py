from django.shortcuts import render, redirect, get_object_or_404
from .models import Nota
from .forms import NotaForm

# list


def listar_notas(request):
    notas = Nota.objects.all().order_by('creado').reverse()
    return render(request, 'listar_notas.html', {'notas': notas})

# create


def crear_nota(request):
    if request.method == "POST":
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_notas')
    else:
        form = NotaForm()
    return render(request, 'crear_notas.html', {'form': form})

# update


def actualizar_nota(request, pk):
    nota = Nota.objects.get(pk=pk)
    if request.method == "POST":
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            return redirect('listar_notas')
    else:
        form = NotaForm(instance=nota)
    return render(request, 'actualizar_notas.html', {'form': form})

# destroy


def borrar_nota(request, pk):
    nota = Nota.objects.get(pk=pk)
    if request.method == 'POST':
        nota.delete()
        return redirect('listar_notas')
    return render(request, 'borrar_notas.html', {'nota': nota})
