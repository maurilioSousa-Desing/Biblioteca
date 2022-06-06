
from django.shortcuts import render, redirect, get_object_or_404
from livros.models import Livro
from livros.forms import LivroForm
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'index.html')


def cria(request):
    if request.method == "POST":
        form = LivroForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            print
            'Livro adicionado com sucesso !'
            return redirect('livros.views.lista')
    else:
        form = LivroForm()
    return render(request, 'cria.html', {'form': form})


def detalhes(request, pk):
    post = get_object_or_404(Livro, pk=pk)
    return render(request, 'detalhes.html', {'post': post})


def atualizar(request, pk):
    post = get_object_or_404(Livro, pk=pk)
    if request.method == "GET":
        form = LivroForm(request.GET, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()

        return redirect('livro.views.detalhes', pk=post.pk)
    else:
        form = LivroForm(instance=post)
    return render(request, 'atualiza.html', {'form': form})


def excluir(request, pk):
    post = get_object_or_404(Livro, pk=pk).delete()
    redirect('livros.views.detalhes')
    return render(request, 'exclui.html', {'post': post})


def lista(request):
    livros = Livro.objects.all()
    return render(request, 'lista.html', locals())
