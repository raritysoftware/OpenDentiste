from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Appointment
from patients.models import Patient


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'date', 'time', 'duration_minutes', 'subject', 'notes']
        widgets = {
            'patient': forms.Select(attrs={
                'class': 'form-select',
                'required': True
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'min': timezone.now().date().isoformat(),
                'required': True
            }),
            'time': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time',
                'step': '300',  # 5 minute intervals
                'required': True
            }),
            'duration_minutes': forms.Select(attrs={
                'class': 'form-select'
            }, choices=[
                (15, _('15 minutes')),
                (30, _('30 minutes')),
                (45, _('45 minutes')),
                (60, _('1 hour')),
                (90, _('1 hour 30 minutes')),
                (120, _('2 hours')),
            ]),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('e.g., Regular checkup, Dental cleaning, Consultation'),
                'required': True
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': _('Any special requirements or additional information')
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['patient'].queryset = Patient.objects.all().order_by('last_name', 'first_name')
        self.fields['patient'].empty_label = _('Select a patient')
        self.fields['duration_minutes'].initial = 30

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date and date < timezone.now().date():
            raise ValidationError(_('Appointment date cannot be in the past.'))
        return date

    def clean_time(self):
        time = self.cleaned_data.get('time')
        if time:
            # Business hours check (9 AM to 6 PM)
            if time.hour < 9 or time.hour >= 18:
                raise ValidationError(_('Appointments are only available between 9:00 AM and 6:00 PM.'))
        return time

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')
        
        if date and time:
            # Check for existing appointments at the same time
            existing = Appointment.objects.filter(
                date=date, 
                time=time
            ).exclude(pk=self.instance.pk if self.instance else None)
            
            if existing.exists():
                raise ValidationError(_('This time slot is already booked. Please choose another time.'))
        
        return cleaned_data
