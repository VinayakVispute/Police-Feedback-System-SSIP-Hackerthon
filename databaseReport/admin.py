from django.contrib import admin
# from django.contrib.admin.sites import site
from .models import stateWisePoliceStation


# Register your models here.
# class reportAdmin(admin.ModelAdmin):
    # list_diplay=('name', 'state', 'police_station', 'how_come', 'time_taken', 'number', 'feedback', 'rating', 'date')


class stateWisePoliceStationAdmin(admin.ModelAdmin):
    list_display = ('state', 'police_station','qr_code')


admin.site.register(stateWisePoliceStation,stateWisePoliceStationAdmin)
# admin.site.register(displayReport, reportAdmin)
