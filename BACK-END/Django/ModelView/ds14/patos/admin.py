from django.contrib import admin
from .models import DonoDoPato, Patinho
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class DonoPatoAdmin(UserAdmin):
    list_display = ['username','is_active','photos']
    fieldsets = UserAdmin.fieldsets + (
        ('Campos Novos',{'fields':('nome_dono','photos','bio')}),

    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Campos Novos',{'fields':('nome_dono','photos','bio')}),
        
    )

admin.site.register(Patinho)
admin.site.register(DonoDoPato, DonoPatoAdmin)
