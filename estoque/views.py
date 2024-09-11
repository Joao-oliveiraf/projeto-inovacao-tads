from django.shortcuts import render
from .forms import EditarProdutoForms,CriarProdutoForms
from .models import Produto


def criar_produto(request):
    form = CriarProdutoForms()
    if request.method == 'POST':
        form = CriarProdutoForms(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'produto.html', {'form':form})

def index(request):
    produtos = Produto.objects.all()
    return render(request, 'index.html', {'produtos': produtos})

def editar_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    form = EditarProdutoForms(instance=produto)
    if request.method == 'POST':
        form = EditarProdutoForms(request.POST, instance=produto)
        if form.is_valid():
            form.save()
    return render(request, 'editar_produto.html',{'form':form, 'produto':produto})
