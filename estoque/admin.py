from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Produto, HistoricalProduto
from simple_history.admin import SimpleHistoryAdmin

class EstoqueFilter(admin.SimpleListFilter):
    title = 'Estoque'

    parameter_name = 'quantidade'

    def lookups(self, request: Any, model_admin: Any) -> list[tuple[str, str]]:
        return [
            ('Alto', ('Estoque Alto')),
            ('Baixo', ('Estoque Baixo')),
        ]
    
    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
        if self.value() == 'Alto':
            queryset = Produto.objects.filter(quantidade__gt=30,quantidade__lt=100)
            return queryset
        if self.value() == 'Baixo':
            return Produto.objects.filter(quantidade__lt=10, quantidade__gt=1)

class ProdutoAdmin(SimpleHistoryAdmin):
    list_display = ('id','nome', 'categoria', 'localizacao', 'quantidade')
    list_display_links = ('id','nome',)
    list_filter = (EstoqueFilter,'localizacao', 'categoria')
    search_fields = ('nome',)
    list_per_page = 15

@admin.register(HistoricalProduto)
class HistoricalProdutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'quantidade', 'data_cadastro', 'history_date', 'history_user', 'history_change_reason',]
    list_filter = ['history_date', 'history_change_reason']

admin.site.register(Produto, ProdutoAdmin)

