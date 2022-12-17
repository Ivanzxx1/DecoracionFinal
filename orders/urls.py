from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.order, name='order'),
    path('orders/pago', views.pago, name='pago'),
    path('orders/confirm', views.confirm, name='confirm')
]