from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django. contrib import messages , auth
from .models import *
from  cart.models import Cart

from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth import authenticate, login as auth_login

from .models import OTP


# Create your views here.
def register(req):
    if req.method=='POST':
        fname=req.POST.get("fname","")
        lname=req.POST.get("lname","")
        email=req.POST.get("email","")
        username=req.POST.get("username","")
        password=req.POST.get("password","")
        cpassword=req.POST.get("cpassword","")
        print(fname,lname,email,username,password,cpassword)
        if password==cpassword:
            print("password verified")
            if User.objects.filter(username=username).exists():
                messages.info(req,"username already exist")
                return redirect('User:Register')
            elif User.objects.filter(email=email).exists():
                messages.info(req,"email already exist")
                return redirect('User:Register')
            else:
                user=User.objects.create_user(first_name=fname,last_name=lname,email=email,username=username,password=password)
                user.save()
                subject = 'Welcome to My Site'
                message = f'Hi {username}, thank you for registering at My Site.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail(subject, message, email_from, recipient_list)
                messages.success(req, 'Registration successful. A confirmation email has been sent to your email address.')
                return redirect('User:Login')
        else:
            messages.info(req,"password not matched")
            return redirect('User:Register')
    return render(req, 'Register.html')


def login(req):
    if req.method == 'POST':
        username = req.POST.get("username", "")
        password = req.POST.get("password", "")
        user = authenticate(req, username=username, password=password)

        if user is not None:
            otp_instance = OTP.objects.create(user=user)
            otp_instance.generate_otp()
            send_mail(
                'Your OTP Code',
                f'Your OTP code is {otp_instance.otp}',
                settings.EMAIL_HOST_USER,
                [user.email]
            )

            req.session['otp_user_id'] = user.id
            return redirect('User:verify_otp')
        else:
            print("User information is invalid")
            return redirect('User:Login')
    return render(req, 'login.html')


def verify_otp(req):
    if req.method == 'POST':
        otp_input = req.POST.get('otp')
        user_id = req.session.get('otp_user_id')
        user = User.objects.get(id=user_id)
        otp_instance = OTP.objects.filter(user=user, otp=otp_input).first()

        if otp_instance and otp_instance.is_valid():
            auth_login(req, user)
            messages.success(req, 'OTP verified successfully. You are now logged in.')
            otp_instance.delete()
            return redirect('mainapp:Home')
        else:
            messages.error(req, 'Invalid or expired OTP.')
    return render(req, 'verify_otp.html')



def logout(req):
    auth.logout(req)
    req.session.pop('user',None)
    return redirect('mainapp:Home')




# def UserDetailsPage(req, id):
#     user=req.session['user']
#     user_obj = User.objects.get(id=id)
#     return render(req, "User.html",)

    
def ADDUserAddress(req,id):
    user=req.session['user']
    profile = User.objects.get(id=id)
    print(user)
    print(profile,"it is the username")
    if req.method == 'POST':
        users=req.POST.get('user','')
        phone = req.POST.get('phone', '')
        address = req.POST.get('address', '')
        pincode= req.POST.get('pincode', '')
        landmark=req.POST.get('landmark', '')
        city=req.POST.get('city', '')
        state=req.POST.get('state', '')
        user_instance = User.objects.get(id=users)
        x = Details(user=user_instance,phone=phone,address=address,pincode=pincode,land_mark=landmark,city=city,state=state)
        x.save()
    return redirect('User:profilepage',id=user_instance.id)
# ---------------------------   UserDashBoard     --------------------------------
def UserDashBoard(req, id):
    user = req.user
    print(user)
    if not user.is_authenticated:
        return redirect('User:Login')
    return render(req, "Userdashboard.html", {'user_id': id})

def Us(req):
    user = req.user
    print(user)
    if not user.is_authenticated:
        return redirect('User:Login')
    return render(req,'userhome.html')

def Profiles(req,id):
    user = req.user
    print(user)
    if not user.is_authenticated:
        return redirect('User:Login')
    user=req.session['user']
    try:
        user_obj = User.objects.get(id=id)
        profile, created = Profile.objects.get_or_create(user=user_obj)
        detail= Details.objects.filter(user=user_obj)
        if 'image' in req.FILES:
            profile.profilepic = req.FILES['image'] 
            profile.save()
    except User.DoesNotExist:
        return redirect('mainapp:Home')
    return render(req,'Userdashboard/profile.html',{"profile":profile,'detail':detail})

def AddressForm(req, id):
    user=req.session['user']
    profile = User.objects.get(id=id)
    return render(req, "Userdashboard/useraddressform.html",{"profile":profile})
def Address(req,id):
    user=req.session['user']
    profile = User.objects.get(id=id)
    detail= Details.objects.filter(user=profile)
    return render(req, "Userdashboard/address.html",{"profile":profile,'detail': detail})
def Carts(req):
    cart = Cart.objects.filter(user=req.session['user'])  # Retrieve cart items\
    # Calculate grand total
    grand_total = sum(item.quantity * item.product.price for item in cart)
    return render(req, 'Userdashboard/cart.html', {'cart': cart ,'grand_total': grand_total})
