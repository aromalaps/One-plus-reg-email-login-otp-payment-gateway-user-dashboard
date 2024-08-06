# # views.py

# from django.shortcuts import render, redirect
# from django.conf import settings
# import paypalrestsdk
# from paypalrestsdk import Payment
# from cart.models import Order, Cart, Product
# import json

# def create_payment(request):
#     user = request.session.get('user')
#     if not user:
#         return redirect('login')  # Ensure the user is logged in

#     # Retrieve the orders for the user
#     orders = Order.objects.filter(user=user)
#     total_amount = sum(order.product.price * order.quantity for order in orders)

#     paypalrestsdk.configure({
#         "mode": settings.PAYPAL_MODE,  # sandbox or live
#         "client_id": settings.PAYPAL_CLIENT_ID,
#         "client_secret": settings.PAYPAL_CLIENT_SECRET,
#     })

#     payment = Payment({
#         "intent": "sale",
#         "payer": {
#             "payment_method": "paypal"},
#         "redirect_urls": {
#             "return_url": "http://localhost:8000/payment/execute/",
#             "cancel_url": "http://localhost:8000/payment/cancel/"},
#         "transactions": [{
#             "item_list": {
#                 "items": [{
#                     "name": order.product.name,
#                     "sku": str(order.product.id),
#                     "price": str(order.product.price),
#                     "currency": "INR",
#                     "quantity": order.quantity} for order in orders]},
#             "amount": {
#                 "total": str(total_amount),
#                 "currency": "INR"},
#             "description": "This is the payment transaction description."}]})

#     if payment.create():
#         for link in payment.links:
#             if link.rel == "approval_url":
#                 approval_url = link.href
#                 return redirect(approval_url)
#     else:
#         return render(request, 'error.html', {'error': payment.error})

# def execute_payment(request):
#     payment_id = request.GET.get('paymentId')
#     payer_id = request.GET.get('PayerID')

#     payment = paypalrestsdk.Payment.find(payment_id)

#     if payment.execute({"payer_id": payer_id}):
#         return render(request, 'success.html', {'payment': payment})
#     else:
#         return render(request, 'error.html', {'error': payment.error})

# def cancel_payment(request):
#     return render(request, 'cancel.html')

# def checkout(request):
#     if request.method == 'POST':
#         Order.checkout(request)  # Process the checkout
#     return render(request, 'checkout.html')









from django.shortcuts import render, redirect
from django.conf import settings
from paypalrestsdk import Payment
import paypalrestsdk
import json

def create_payment(request):
    if request.method == 'POST':
        payment = Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"},
            "redirect_urls": {
                "return_url": request.build_absolute_uri('/payments/execute/'),
                "cancel_url": request.build_absolute_uri('/payments/cancel/')},
            "transactions": [{
                "item_list": {
                    "items": [{
                        "name": "Item Name",
                        "sku": "item",
                        "price": "5.00",
                        "currency": "USD",
                        "quantity": 1}]},
                "amount": {
                    "total": "5.00",
                    "currency": "USD"},
                "description": "This is the payment transaction description."}]})

        if payment.create():
            for link in payment.links:
                if link.rel == "approval_url":
                    approval_url = str(link.href)
                    return redirect(approval_url)
        else:
            print(payment.error)

    return render(request, 'payment/payment_form.html')

def execute_payment(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')
    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        return render(request, 'payment/payment_success.html')
    else:
        return render(request, 'payment/payment_error.html')

def cancel_payment(request):
    return render(request, 'payment/payment_cancelled.html')
