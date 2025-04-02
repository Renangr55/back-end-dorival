from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserAdmSite

# Register your models here.
admin.site.register(UserAdmSite)

class UserAdminstrator(UserAdmSite):
    list_display = ('usernmame','email')