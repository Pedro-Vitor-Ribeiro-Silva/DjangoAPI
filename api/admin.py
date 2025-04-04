from django.contrib import admin
from .models import Pessoa

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao','image') 
    search_fields = ('nome',)
