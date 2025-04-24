from django.contrib import admin
from .models import Client, HealthProgram
# Register your models here.
@admin.register(HealthProgram)
class HealthProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'start_date', 'end_date', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('start_date', 'end_date')
    ordering = ('-created_at',)

    
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'gender', 'address', 'phone_number', 'email', 'health_program', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'email')
    filter_horizontal = ('health_program',)