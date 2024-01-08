from django.contrib import admin
from .models import Representative, Activity_news, Villagepublic


class RepresentativeAdmin(admin.ModelAdmin):
    list_display = ('image', 'first_name', 'last_name', 'position', 'phone_number')
    
admin.site.register(Representative, RepresentativeAdmin)


class Activity_newsAdmin(admin.ModelAdmin):
    list_display = ('image', 'text', 'date', 'time')

admin.site.register(Activity_news, Activity_newsAdmin)

class VillagepublicAdmin(admin.ModelAdmin):
    list_display = ('image', 'first_name', 'last_name', 'position', 'phone_number')

admin.site.register(Villagepublic, VillagepublicAdmin)