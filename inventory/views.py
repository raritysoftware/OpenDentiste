from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.utils.translation import gettext_lazy as _
from django.db import models
from .models import StockItem


class StockItemListView(ListView):
    model = StockItem
    template_name = 'inventory/list.html'
    context_object_name = 'stock_items'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['low_stock_items'] = StockItem.objects.filter(quantity__lte=models.F('minimum_stock')).count()
        return context


class StockItemDetailView(DetailView):
    model = StockItem
    template_name = 'inventory/detail.html'
    context_object_name = 'stock_item'
