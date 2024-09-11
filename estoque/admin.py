from django.contrib import admin
from .models import Produto
from simple_history.admin import SimpleHistoryAdmin

class ProdutoAdmin(SimpleHistoryAdmin):
    list_display = ('id','nome', 'categoria', 'localizacao', 'quantidade')
    list_display_links = ('id','nome',)
    list_filter = ('localizacao', 'quantidade')
    

admin.site.register(Produto, ProdutoAdmin)
