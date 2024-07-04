from django.contrib import admin
from .models import *
# Register your models here.



# class TransferAdmin(admin.ModelAdmin):
#     list_display = ('chofer', 'patente', 'posicion')

admin.site.register(Transfer)
admin.site.register(Chofer)
admin.site.register(Cliente)
admin.site.register(Ticket)