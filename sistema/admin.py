
from django.contrib import admin

from sistema import models

# Aqui fica o registro do Usuário
@admin.register(models.Usuário)
class UsuárioAdmin(admin.ModelAdmin):
    list_display = ('id','nome','sobrenome','email','ativo',)   

# Register your models here.


# aqui fica o registro do filme
    
@admin.register(models.Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_do_filme', 'ano_de_lancamento', 'estudio', 'genero',)

# aqui fica o registro do genero

@admin.register(models.Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')