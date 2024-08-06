# from django.urls import path
# from .views import create_payment, execute_payment, cancel_payment

# app_name='payment'


# urlpatterns = [
#     path('payment/create/', create_payment, name='create-payment'),
#     path('payment/execute/', execute_payment, name='execute-payment'),
#     path('payment/cancel/', cancel_payment, name='cancel-payment'),
# ]

from django.urls import path
from .views import create_payment, execute_payment, cancel_payment

app_name = 'payment'

urlpatterns = [
    path('create/', create_payment, name='create-payment'),
    path('execute/', execute_payment, name='execute-payment'),
    path('cancel/', cancel_payment, name='cancel-payment'),
]
