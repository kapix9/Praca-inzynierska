
from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Cwiczenie, Seria



class CwiczenieAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'opis', 'video_url')

class SeriaAdmin(admin.ModelAdmin):
    list_display = ('cwiczenie', 'ilosc_powtorzen', 'ilosc_serii', 'obciazenie', 'uwagi', 'tempo', 'nagraj',  )
    list_filter = ('podopieczny','dzien_tygodnia')
# Register your models here.

admin.site.register(Cwiczenie,CwiczenieAdmin)
admin.site.register(Seria, SeriaAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)
