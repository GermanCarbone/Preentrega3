from django.urls import path, include
from .views import *

urlpatterns = [

    path('', index, name="inicio" ),
    path('establecimientos/', establecimientos, name="establecimientos"),
    path('distritos/', distritos, name="distritos"),
    path('fiscales/', fiscales, name="fiscales"),

    path('fiscalform/', fiscalForm, name='fiscal_form')
]