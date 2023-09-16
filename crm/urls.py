from django.contrib import admin
from django.urls import path
from core.views import success, success2, success3

urlpatterns = [
    path('ajax/', success, name='success_page'),
    path('ajax2/', success2, name='success_page2'),
    path('ajax3/', success3, name='success_page3')
]