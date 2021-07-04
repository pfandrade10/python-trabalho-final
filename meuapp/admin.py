from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(ContaPagar)
admin.site.register(Classificacao)
admin.site.register(ContaReceber)
