from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'date', 'time', 'subject', 'status', 'created_at']
    list_filter = ['status', 'date', 'created_at']
    search_fields = ['patient__first_name', 'patient__last_name', 'subject']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'date'
    
    fieldsets = (
        (_('Appointment Details'), {
            'fields': ('patient', 'date', 'time', 'duration_minutes', 'subject')
        }),
        (_('Status & Notes'), {
            'fields': ('status', 'notes')
        }),
        (_('System Information'), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('patient')
