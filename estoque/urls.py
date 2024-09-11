from django.urls import path
from .views import criar_produto, index,editar_produto

urlpatterns = [
    path('criar_produto', criar_produto, name='criar_produto'),
    path('', index, name='index'),
    path('editar_produto/<int:produto_id>', editar_produto, name='editar_produto')
]
