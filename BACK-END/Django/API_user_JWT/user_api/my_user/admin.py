from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserAdmSite

# Register your models here.
admin.site.register(User)

class UserAdminstrator(UserAdmSite):
    list_display = ('usernmame')