from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),

    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register,name='register'),

    path('products/', views.products,name='products'),

    path('customer/<str:pk>/', views.customer,name='customers'),
    path('customer_create',views.create_customer,name='create_customer'),
    path('customer_update/<str:pk>',views.update_customer,name='update_customer'),

    path('order_create_bulk/<str:pk>',views.create_bulk_order,name='create_bulk_order'),
    path('order_create',views.create_order,name='create_order'),
    path('delete_order/<str:pk>',views.delete_order,name='delete_order'),
    path('update_order/<str:pk>',views.update_order,name='update_order')
]
