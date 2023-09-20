from django.urls import path
from . import views

urlpatterns = [
       path('vopros-otvet/', views.vopros_otvet, name='vopros_otvet'),
       path('reviews/', views.reviews, name='reviews'),
]