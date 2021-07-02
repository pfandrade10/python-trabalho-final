from django.contrib import admin

# Register your models here.
from .models import *
from .models.pessoa import Pessoa

admin.site.register(Pessoa)
admin.site.register(Telefone)
admin.site.register(Departamento)
