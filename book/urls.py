from django.urls import path
from django.views.generic import *
from .models import Book

app_name = 'book'
urlpatterns = [
    path('', ListView.as_view(model=Book), name='list'),
    path('detail/<pk>/',DetailView.as_view(model=Book), name='detail'),
    path('create/', CreateView.as_view(model=Book, fields='__all__'), name='create'),
    path('create/', UpdateView.as_view(model=Book, fields='__all__'), name='update'),
]