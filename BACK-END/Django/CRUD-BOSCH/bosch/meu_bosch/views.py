from django.shortcuts import render,redirect,get_object_or_404
from .models import Livro
from .form import LivroForm
from .filters import LivroFilter

# Create your views here.
def livro_read(request):
    livros = Livro.objects.all()
    return render(request, "livro_read.html", {"livros" : livros})

def livro_create(request):
    if request.method == "POST":
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livro_read')
    else:
        form = LivroForm()

    return render(request, 'livro_form.html', {'form' : form})

def livro_update(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('livro_read')
    else: 
        form = LivroForm(instance=livro)

    return render(request,'livro_form.html', {'form' : form})

def livro_delete(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('livro_read')
    return render(request, 'livro_confirm_delete.html' , {'livro': livro})

def livro_list(request):
    livros = Livro.objects.all()
    filtro = LivroFilter(request.GET, queryset=livros)
    return render(request, 'livro_list.html', {'filter' : filtro})
