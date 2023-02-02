from django.shortcuts import render, resolve_url, redirect
from django.http import HttpRequest, HttpResponse
from datetime import date
import random
import string

# Create your views here.

def home_page(request : HttpRequest):
    today = date.today()
    context = {"today" : today}
    cookies = request.COOKIES
    riyadh_page_url = resolve_url("saudi_cites:riyadh")
    response =  render(request, "saudi_cites/home_page.html",context )
    response.set_cookie("last_visit", today)
    return response,render(request, 'saudi_cites/home_page.html')







def home_page(request : HttpRequest):
    today = date.today()
    context = {"today" : today}

    cookies = request.COOKIES
    return render(request, "saudi_cites/home_page.html",context )



def consent_to_TOS(request : HttpRequest):
    response = redirect("saudi_cites:home_page")
    response.set_cookie("consent", "Yes", max_age=60*60*24*7)
    return response




def set_dark_mode(request : HttpRequest):
    response = redirect("saudi_cites:home_page")
    response.set_cookie("mode", "dark", max_age=60*60*24*7)
    return response


def set_light_mode(request : HttpRequest):
    response = redirect("saudi_cites:home_page")
    response.set_cookie("mode", "light", max_age=60*60*24*7)
    return response




def riyadh(request : HttpRequest):
    return render(request, "saudi_cites/riyadh.html")

def alaula(request : HttpRequest):
    return render(request, "saudi_cites/alaula.html")

def tabuk(request : HttpRequest):
    return render(request, "saudi_cites/tabuk.html")

def aldhahran(request : HttpRequest):
    return render(request, "saudi_cites/aldhahran.html")









