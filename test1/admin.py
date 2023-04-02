from django.contrib import admin
from .models import *

# Register your models here.

class AdminRegister(admin.ModelAdmin):
    list_display = ["name","loginid","password","mobile","email","locality","city","state"]

admin.site.register(UserRegister,AdminRegister)


# admin user name : test1
# admin password : Test@2244