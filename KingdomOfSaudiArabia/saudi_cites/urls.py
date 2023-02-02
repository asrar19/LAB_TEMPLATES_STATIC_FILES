from django.urls import path
from . import views

app_name = "saudi_cites"

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("riyadh/", views.riyadh, name="riyadh"),
    path("/tabuk/", views.tabuk, name="tabuk"),
    path("/aldhahran/", views.aldhahran, name="aldhahran"),
    path("/alaula/", views.alaula, name="alaula"),
]

