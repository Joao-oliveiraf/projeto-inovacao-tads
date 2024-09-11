from django import forms
from .models import Produto

class ProdutoForms(forms.ModelForm):
    class Meta:
        model = Produto
        exclude = ['data_cadastro', '_change_reason']
        widgets = {
            'categoria': forms.Select(),
            'localizacao': forms.Select()
        }
