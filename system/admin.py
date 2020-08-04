from django.contrib import admin
from .models import Usuario, Jogo, Categoria


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', )


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', )


class JogoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user_attack', 'user_defense')
    list_display_links = ('id', 'name')
    search_fields = ('name', )

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Jogo, JogoAdmin)
