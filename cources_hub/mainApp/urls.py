from django.urls import path
from .views import *

urlpatterns = [
    path('', mainPage, name='online_url'),
    path('kyiv/', kyiv, name='kyiv_url'),
    path('dnipro/', dnipro, name='dnipro_url'),
    path('lviv/', lviv, name='lviv_url'),
    path('kharkiv/', kharkiv, name='kharkiv_url'),
    path('odessa/', odessa, name='odessa_url'),
    path('<str:slug>/', eventdetail, name='eventdetail_url'),
]
