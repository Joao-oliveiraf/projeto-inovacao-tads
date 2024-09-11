from django.shortcuts import render
from .forms import ProdutoForms


def produto(request):
    form = ProdutoForms()
    if request.method == 'POST':
        form = ProdutoForms(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'produto.html', {'form':form})
