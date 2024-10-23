from django.urls import path,include
from . import views
urlpatterns = [
    path('/',views.names,name="names"),
    path('items/', views.item_list, name='item-list'),
    path('items/<int:pk>/', views.item_detail, name='item-detail'),
]
