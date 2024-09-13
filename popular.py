import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from estoque.models import Produto
import random

def criar():
    produtos = [
    {'produto': 'Computador', 'categoria': 'E'},
    {'produto': 'Geladeira', 'categoria': 'D'},
    {'produto': 'Micro-ondas', 'categoria': 'D'},
    {'produto': 'Smartphone', 'categoria': 'E'},
    {'produto': 'Televisão', 'categoria': 'E'},
    {'produto': 'Máquina de Lavar Roupas', 'categoria': 'D'},
    {'produto': 'Ar-condicionado', 'categoria': 'D'},
    {'produto': 'Tablet', 'categoria': 'E'},
    {'produto': 'Forno Elétrico', 'categoria': 'D'},
    {'produto': 'Roteador Wi-Fi', 'categoria': 'E'},
    {'produto': 'Batedeira', 'categoria': 'D'},
    {'produto': 'Liquidificador', 'categoria': 'D'},
    {'produto': 'Aspirador de Pó', 'categoria': 'D'},
    {'produto': 'Smartwatch', 'categoria': 'E'},
    {'produto': 'Headphone', 'categoria': 'E'},
    {'produto': 'Mouse', 'categoria': 'E'},
    {'produto': 'Teclado', 'categoria': 'E'},
    {'produto': 'Monitor', 'categoria': 'E'},
    {'produto': 'Ventilador', 'categoria': 'D'},
    {'produto': 'Ferro de Passar', 'categoria': 'D'},
    {'produto': 'Impressora', 'categoria': 'E'},
    {'produto': 'Toalha de Banho', 'categoria': 'CMB'},
    {'produto': 'Jogo de Lençol', 'categoria': 'CMB'},
    {'produto': 'Cafeteira', 'categoria': 'D'},
    {'produto': 'Travesseiro', 'categoria': 'CMB'},
    {'produto': 'Cobertor', 'categoria': 'CMB'},
    {'produto': 'Edredom', 'categoria': 'CMB'},
    {'produto': 'Cortina', 'categoria': 'CMB'},
    {'produto': 'Jogo de Toalhas', 'categoria': 'CMB'},
    {'produto': 'Panela Elétrica', 'categoria': 'D'},
    {'produto': 'Chaleira Elétrica', 'categoria': 'D'},
    {'produto': 'Abajur', 'categoria': 'D'},
    {'produto': 'Secador de Cabelos', 'categoria': 'D'},
    {'produto': 'Espelho', 'categoria': 'D'},
    {'produto': 'Capa de Sofá', 'categoria': 'CMB'},
    {'produto': 'Jogo de Tapetes', 'categoria': 'CMB'},
    {'produto': 'Frigobar', 'categoria': 'D'},
    {'produto': 'Lava-louças', 'categoria': 'D'},
    {'produto': 'Smart Speaker', 'categoria': 'E'},
    {'produto': 'Projetor', 'categoria': 'E'},
    {'produto': 'Câmera de Segurança', 'categoria': 'E'},
    {'produto': 'Drone', 'categoria': 'E'},
    {'produto': 'Home Theater', 'categoria': 'E'},
    {'produto': 'Som Bluetooth', 'categoria': 'E'},
    {'produto': 'Relógio de Mesa', 'categoria': 'D'},
    {'produto': 'Aquecedor', 'categoria': 'D'},
    {'produto': 'Panela de Pressão Elétrica', 'categoria': 'D'},
    {'produto': 'Porta Travesseiro', 'categoria': 'CMB'},
    {'produto': 'Lençol Avulso', 'categoria': 'CMB'}
]

    choices_localizacao = ['R1','R2','R3']
    for item in produtos:
        localizacao = random.choice(choices_localizacao)
        p = Produto(
            nome = item['produto'],
            categoria=item['categoria'],
            localizacao=localizacao,
            quantidade=random.randint(1,75),
            preco=random.randint(20, 300)
        )
        p.save()

if __name__ == '__main__':
    criar()

