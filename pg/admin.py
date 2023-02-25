from django.contrib import admin

# Register your models here.
from .models import pg_owner
from .models import student
from .models import adm

admin.site.register(pg_owner)
admin.site.register(student)
admin.site.register(adm)