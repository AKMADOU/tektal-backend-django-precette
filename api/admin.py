from django.contrib import admin

from api.models import *


#from __future__ import unicode_literals

from django.contrib import admin



from import_export.admin import ImportExportModelAdmin
from import_export import resources


# Register our "Message" model with the Django Admin/


# class UserAdmin(admin.ModelAdmin):
#     readonly_fields = ('date_joined',)
#     list_display = ('email', )
    
class VideosResource(resources.ModelResource):

    class Meta:
        model = Quartier

class QuartierAdmin(admin.ModelAdmin):
    list_display=('nom_quartier','date','ville')
    list_filter=('nom_quartier',)
    search_fields=('nom_quartier',)
    

admin.site.register(Quartier,  QuartierAdmin)
admin.site.register(User)


        

