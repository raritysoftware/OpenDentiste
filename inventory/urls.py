from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.StockItemListView.as_view(), name='list'),
    path('<int:pk>/', views.StockItemDetailView.as_view(), name='detail'),
]
