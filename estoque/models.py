from django.db import models
from simple_history.models import HistoricalRecords

class Produto(models.Model):
    CHOICES_CATEGORIA = [
        ('E', 'Eletronicos'),
        ('D', 'Domésticos'),
        ('CMB', 'Cama, Mesa e Banho'),
    ]
    CHOICES_LOCALIZACAO = [
        ('R1', 'Rua 1'),
        ('R2', 'Rua 2'),
        ('R3', 'Rua 3'),
    ]
    CHOICES_RAZAO = [
        ('Compra', 'Compra'),
        ('Venda', 'Venda'),
    ]
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=True,
        verbose_name='Nome do Produto'
    )
    categoria = models.CharField(
        choices=CHOICES_CATEGORIA,
        max_length=5,
        null=False,
        blank=False
    )
    localizacao = models.CharField(
        choices=CHOICES_LOCALIZACAO,
        max_length=5,
        blank=False,
        null=False
    )
    quantidade = models.IntegerField(
        null=False,
        blank=False
    )
    preco = models.DecimalField(
        decimal_places=2,
        blank=False,
        null=False,
        max_digits=10
    )
    data_cadastro = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False
    )

    history = HistoricalRecords()

    _change_reason = models.CharField(
        choices=CHOICES_RAZAO,
        max_length=255,
        blank=True,
        verbose_name='Razão da alteração',
        default='Criar'
    )
    
    def __str__(self) -> str:
        return self.nome
    


