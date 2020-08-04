from django.contrib import admin
from.models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', )

admin.site.register(Usuario, UsuarioAdmin)
