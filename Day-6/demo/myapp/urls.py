from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('ping/', views.ping, name='ping'),
    path('items/', views.allItems, name='all_items'),
    path('items/<int:item_id>/', views.getItem, name='get_item'),
    path('create/', views.createItem, name='create_item')
]
