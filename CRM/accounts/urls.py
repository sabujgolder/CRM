from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('products/', views.products,name='products'),
    path('customer/<str:pk>/', views.customer,name='customers'),
    path('order_create',views.create_order,name='create_order')
]
