from django.contrib import admin
from .models import Zaal, FaceUser


class ZaalAdmin(admin.ModelAdmin):
    """
    Configuration to display 'Zaal' models in the Django admin site.
    """
    # Fields to be used in the form for creating 'Zaal' objects
    fields = ('naam', 'locatie', 'aantal_plaatsen')
    # Fields to lookup when using the search bar in Django admin
    search_fields = ('naam', 'locatie', 'aantal_plaatsen')
    # Fields to be displayed in the Django admin overview for 'Zaal'
    list_display = ('naam', 'locatie', 'aantal_plaatsen')


class FaceUserAdmin(admin.ModelAdmin):
    """
       Configuration to display 'FaceUser' models in the Django admin site.
       """
    # Fields to be used in the form for creating 'FaceUser' objects
    fields = ('face_id', 'first_name', 'last_name', 'email')


# registers Zaal andhis configuration ZaalAdmin in the Django-admin site
admin.site.register(Zaal, ZaalAdmin)
admin.site.register(FaceUser, FaceUserAdmin)
