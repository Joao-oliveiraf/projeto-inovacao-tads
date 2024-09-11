from django import forms
from .models import Produto

class EditarProdutoForms(forms.ModelForm):
    class Meta:
        model = Produto
        exclude = ['categoria', 'nome']
        widgets = {
            'localizacao': forms.Select()
        }
        
    
    def clean_nome(self):
        valor_inicial = self.instance.nome
        valor_enviado = self.cleaned_data.get("nome")

        if valor_inicial != valor_enviado:
            raise forms.ValidationError('Não é permitido alterar o nome do produto!')
        return valor_inicial
    

    def clean_categoria(self):
        valor_inicial = self.instance.categoria
        valor_enviado = self.cleaned_data.get('categoria')

        if valor_enviado != valor_inicial:
            raise forms.ValidationError('A categoria não pode ser alterada!')
        return valor_inicial


class CriarProdutoForms(forms.ModelForm):
    class Meta:
        model = Produto
        exclude = ['data_cadastro']