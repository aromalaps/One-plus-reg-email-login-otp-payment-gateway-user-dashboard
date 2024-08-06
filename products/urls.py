from django.urls import path
from . import views

app_name = 'Products'
urlpatterns = [
    path('products/',views.Products, name='products'),
    path('<slug:c_slug>/',views.Products,name='product_by_category'),
    path('details/<int:id>',views.Details, name='detail'),
]

#'Products:product'
