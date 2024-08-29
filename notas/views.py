from django.shortcuts import render, redirect
from .models import Nota
from .forms import NotaForm


def lista_notas(request):
    notas = Nota.objects.all()  # .order_by('creado').reverse()
    return render(request, 'listar_notas.html', {'notas': notas})


def crear_nota(request):
    if request.method == "POST":
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_notas')
    else:
        form = NotaForm()
    return render(request, 'crear_notas.html', {'form': form})
