from django.shortcuts import render

# Create your views here.
from app.models import *


def home(request):
    wheels = Wheel.objects.all()
    navs = Nav.objects.all()
    mustbuys = Mustbuy.objects.all()

    shop1 = Shop.objects.first()
    shops2_3 = Shop.objects.all()[1:3]
    shop4_7 = Shop.objects.all()[3:7]
    shops8_11 = Shop.objects.all()[7:11]
    data = {
       "wheels":wheels,
        "navs":navs,
        "mustbuys":mustbuys,
        "shop1":shop1,
        "shop2_3":shops2_3,
        "shop4_7":shop4_7,
        "shop8_11":shops8_11,
    }

    return render(request,'home/home.html',context=data)


def market(request):
    return render(request,'market/market.html')


def cart(request):
    return render(request,'cart/cart.html')


def mine(request):
    return render(request,'mine/mine.html')