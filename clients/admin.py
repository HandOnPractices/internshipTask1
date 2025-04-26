from django.contrib import admin
from .models import HealthProgram, Client

@admin.register(HealthProgram)
class HealthProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'created_at')
    search_fields = ('name', 'description')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'gender', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('gender', 'health_program')