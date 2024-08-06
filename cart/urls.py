from django.urls import path
from .import views

app_name='Cart'
urlpatterns = [
   
    path('add_quantity/<int:id>',views.addcart,name='addcart'),
    path('cart_page/',views.cart_page,name='cart_page'),
    path('quantity_remove/<int:id>',views.quantity_remove,name='quantityremove'),
    path('removesingle/<int:id>',views.RemoveX,name='removeX'),
    path('Check_Out/', views.Checkout, name='checkout'),
    path('ClearAll/', views.ClearCart, name='clearall'),
]
# Cart:clearall




















# Cart:cartpage