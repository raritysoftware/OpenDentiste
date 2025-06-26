from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('', views.AppointmentListView.as_view(), name='list'),
    path('book/', views.AppointmentCreateView.as_view(), name='book'),
    path('<int:pk>/', views.AppointmentDetailView.as_view(), name='detail'),
]
