from django.shortcuts import render,redirect
from .models import NewProduct
# Create your views here.
def Home(req):
    return render(req,'index.html')


