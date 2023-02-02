from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date



def home_page(request : HttpRequest):
    today = date.today()
    context = {"today" : today}
    return render(request, "saudi_cites/home_page.html", context )




def riyadh(request : HttpRequest):
    return render(request, "saudi_cites/riyadh.html")

def alaula(request : HttpRequest):
    return render(request, "saudi_cites/alaula.html")

def tabuk(request : HttpRequest):
    return render(request, "saudi_cites/tabuk.html")

def aldhahran(request : HttpRequest):
    return render(request, "saudi_cites/aldhahran.html")


