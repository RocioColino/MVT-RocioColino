from django.contrib import admin

from .models import Informacion

class InformacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'altura', 'nacimiento')

admin.site.register(Informacion, InformacionAdmin)

