from django.contrib import admin
from .models import Zaal


# Register your models here.
class ZaalAdmin(admin.ModelAdmin):
    fields = ('naam', 'locatie', 'aantal_plaatsen')
    search_fields = ('naam', 'locatie', 'aantal_plaatsen')
    list_display = ('naam', 'locatie', 'aantal_plaatsen')


admin.site.register(Zaal, ZaalAdmin)
