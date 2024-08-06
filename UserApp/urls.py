from django.urls import path
from .import views

app_name='User'
urlpatterns = [
   
    path('user/',views.register,name='Register'),
    path('login/',views.login,name='Login'),
    path('logout/',views.logout,name='Logout'),
    path('useradderess/<int:id>',views.ADDUserAddress,name='useradderess'),
    path('addressform/<int:id>', views.AddressForm, name='addressform'),
    path('address/<int:id>', views.Address, name='address'),
    path('userdashboard/<int:id>',views.UserDashBoard,name='userdashboard'),
    path('us/',views.Us,name='us'),
    path('profilepage/<int:id>',views.Profiles,name='profilepage'),
    path('cart_page/',views.Carts,name='cart_page'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),

]
# url 'User:profile'
