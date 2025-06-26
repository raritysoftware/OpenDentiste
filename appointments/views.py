from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from .models import Appointment
from .forms import AppointmentForm


class AppointmentListView(ListView):
    model = Appointment
    template_name = 'appointments/list.html'
    context_object_name = 'appointments'
    paginate_by = 10
    ordering = ['date', 'time']


class AppointmentDetailView(DetailView):
    model = Appointment
    template_name = 'appointments/detail.html'
    context_object_name = 'appointment'


class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointments/book.html'
    success_url = reverse_lazy('appointments:list')
    
    def form_valid(self, form):
        form.instance.status = 'pending'
        messages.success(
            self.request, 
            _('Appointment booked successfully! You will be contacted for confirmation.')
        )
        return super().form_valid(form)
