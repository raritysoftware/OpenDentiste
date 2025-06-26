from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'email', 'created_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['first_name', 'last_name', 'phone', 'email']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        (_('Personal Information'), {
            'fields': ('first_name', 'last_name', 'date_of_birth', 'phone', 'email')
        }),
        (_('Address & Contact'), {
            'fields': ('address', 'emergency_contact')
        }),
        (_('Medical Information'), {
            'fields': ('medical_notes',)
        }),
        (_('System Information'), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
