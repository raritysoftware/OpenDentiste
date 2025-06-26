from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from .models import StockItem


@admin.register(StockItem)
class StockItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity_display', 'unit', 'stock_status_display', 'expiry_date', 'supplier']
    list_filter = ['unit', 'supplier', 'created_at', 'expiry_date']
    search_fields = ['name', 'description', 'supplier']
    readonly_fields = ['created_at', 'updated_at', 'stock_status_display']
    
    fieldsets = (
        (_('Item Information'), {
            'fields': ('name', 'description', 'supplier')
        }),
        (_('Stock Details'), {
            'fields': ('quantity', 'unit', 'minimum_stock', 'cost_per_unit')
        }),
        (_('Expiry Information'), {
            'fields': ('expiry_date',)
        }),
        (_('System Information'), {
            'fields': ('stock_status_display', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def quantity_display(self, obj):
        return f"{obj.quantity} {obj.get_unit_display()}"
    quantity_display.short_description = _('Quantity')
    
    def stock_status_display(self, obj):
        status = obj.stock_status
        if status == 'expired':
            color = 'red'
            text = _('Expired')
        elif status == 'low':
            color = 'orange'
            text = _('Low Stock')
        else:
            color = 'green'
            text = _('Normal')
        
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            color, text
        )
    stock_status_display.short_description = _('Stock Status')
