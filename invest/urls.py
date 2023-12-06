from django.urls import path
from . import views

urlpatterns = [
    path('invest/', views.InvestPost, name='InvestPost'),
    path('invest/<slug:slug_invest>', views.InvestDeteil, name='InvestDeteilPosts'),

   # path('catalog/<slug:slug_dom>/', views.DetailPosts, name='DetailPosts'),  # new

]