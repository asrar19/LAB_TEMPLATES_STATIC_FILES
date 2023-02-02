from django.urls import path
from . import views

app_name = "saudi_cites"

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("riyadh/", views.riyadh, name="riyadh"),
    path("tabuk/", views.tabuk, name="tabuk"),
    path("aldhahran/", views.aldhahran, name="aldhahran"),
    path("alaula/", views.alaula, name="alaula"),
    path("consent/tos/", views.consent_to_TOS, name="consent_to_tos"),
    path("mode/dark/", views.set_dark_mode, name="mode_dark"),
    path("mode/light/", views.set_light_mode, name="mode_light"),

]

