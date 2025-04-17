from django.contrib import admin
from .models import Usuario
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class UsuarioAdmin(UserAdmin):
    list_display = ['username','biografia','idade']
    fieldsets = UserAdmin.fieldsets + (
        ('Campos Novos',{'fields': ('telefone','biografia','escolaridade')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Campos Novos',{'fields': ('telefone','biografia','escolaridade')}),
    )

admin.site.register(Usuario, UsuarioAdmin)