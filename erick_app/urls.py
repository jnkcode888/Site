from django.urls import path
from erick_app import views



urlpatterns = [
    path('', views.home,name='my_home'),
    path('error/',views.error,name='error'),
    path('payment/', views.payment, name='payment'),
    path('history/',views.history,name='history'),
    path('menu/',views.menu,name='menu'),
    path('menu/payment/', views.payment, name='payment'),
    path('menu/payment/<int:total>/', views.payment, name='payment'),
    path('menu/payment/history/', views.payment_history, name='payment_history'),
    path('menu/payment/history/<int:student_id>/', views.payment_history, name='payment_history')
]