from django.db import models

class Produto(models.Model):
    CHOICES_CATEGORIA = [
        ('E', 'Eletronicos'),
        ('D', 'Domésticos'),
        ('CMB', 'Casa, Mesa e Banho'),
    ]
    CHOICES_LOCALIZACAO = [
        ('R1', 'Rua 1'),
        ('R2', 'Rua 2'),
        ('R3', 'Rua 3'),
    ]
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=True
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
        null=False
    )
    data_cadastro = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False
    )

