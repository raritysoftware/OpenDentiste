from django.db import models
from django.utils.translation import gettext_lazy as _


class StockItem(models.Model):
    """Stock item model for managing clinic inventory"""
    
    UNIT_CHOICES = [
        ('piece', _('Piece')),
        ('box', _('Box')),
        ('bottle', _('Bottle')),
        ('tube', _('Tube')),
        ('pack', _('Pack')),
        ('kg', _('Kilogram')),
        ('liter', _('Liter')),
    ]
    
    name = models.CharField(_('Name'), max_length=200)
    description = models.TextField(_('Description'), blank=True, null=True)
    quantity = models.PositiveIntegerField(_('Quantity'), default=0)
    unit = models.CharField(_('Unit'), max_length=20, choices=UNIT_CHOICES, default='piece')
    minimum_stock = models.PositiveIntegerField(_('Minimum Stock Level'), default=5)
    expiry_date = models.DateField(_('Expiry Date'), blank=True, null=True)
    supplier = models.CharField(_('Supplier'), max_length=200, blank=True, null=True)
    cost_per_unit = models.DecimalField(_('Cost per Unit'), max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    class Meta:
        verbose_name = _('Stock Item')
        verbose_name_plural = _('Stock Items')
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.quantity} {self.get_unit_display()})"

    @property
    def is_low_stock(self):
        return self.quantity <= self.minimum_stock

    @property
    def is_expired(self):
        if not self.expiry_date:
            return False
        from django.utils import timezone
        return self.expiry_date < timezone.now().date()

    @property
    def stock_status(self):
        if self.is_expired:
            return 'expired'
        elif self.is_low_stock:
            return 'low'
        else:
            return 'normal'
