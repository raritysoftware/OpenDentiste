from django.db import models
from django.utils.translation import gettext_lazy as _
from patients.models import Patient


class Appointment(models.Model):
    """Appointment model for managing patient appointments"""
    
    STATUS_CHOICES = [
        ('pending', _('Pending')),
        ('confirmed', _('Confirmed')),
        ('completed', _('Completed')),
        ('cancelled', _('Cancelled')),
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name=_('Patient'))
    date = models.DateField(_('Date'))
    time = models.TimeField(_('Time'))
    duration_minutes = models.PositiveIntegerField(_('Duration (minutes)'), default=30)
    subject = models.CharField(_('Subject'), max_length=200)
    notes = models.TextField(_('Notes'), blank=True, null=True)
    status = models.CharField(_('Status'), max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    class Meta:
        verbose_name = _('Appointment')
        verbose_name_plural = _('Appointments')
        ordering = ['date', 'time']
        unique_together = ['date', 'time']  # Prevent double booking

    def __str__(self):
        return f"{self.patient.full_name} - {self.date} {self.time}"

    @property
    def is_upcoming(self):
        from django.utils import timezone
        return self.date >= timezone.now().date() and self.status in ['pending', 'confirmed']
