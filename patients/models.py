from django.db import models
from django.utils.translation import gettext_lazy as _


class Patient(models.Model):
    """Patient model for storing patient information"""
    
    first_name = models.CharField(_('First Name'), max_length=100)
    last_name = models.CharField(_('Last Name'), max_length=100)
    phone = models.CharField(_('Phone'), max_length=20)
    email = models.EmailField(_('Email'), blank=True, null=True)
    date_of_birth = models.DateField(_('Date of Birth'), blank=True, null=True)
    address = models.TextField(_('Address'), blank=True, null=True)
    emergency_contact = models.CharField(_('Emergency Contact'), max_length=200, blank=True, null=True)
    medical_notes = models.TextField(_('Medical Notes'), blank=True, null=True)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    class Meta:
        verbose_name = _('Patient')
        verbose_name_plural = _('Patients')
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
