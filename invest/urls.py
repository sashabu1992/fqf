from django.urls import path
from . import views

urlpatterns = [
    path('invest/', views.InvestPost, name='InvestPost'),
    path('invest/1/', views.InvestDeteil, name='InvestDeteil'),

   # path('catalog/<slug:slug_dom>/', views.DetailPosts, name='DetailPosts'),  # new

]