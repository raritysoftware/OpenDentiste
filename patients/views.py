from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .models import Patient
from .forms import PatientForm


class PatientListView(ListView):
    model = Patient
    template_name = 'patients/list.html'
    context_object_name = 'patients'
    paginate_by = 10


class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patients/detail.html'
    context_object_name = 'patient'


class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patients/create.html'
    success_url = reverse_lazy('patients:list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        return response
