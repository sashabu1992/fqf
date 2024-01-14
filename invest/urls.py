from django.urls import path
from . import views

urlpatterns = [
    path('invest/', views.InvestPost, {'template':'invest/invest_list.html'}, name='InvestPost'),
    path('invest/<slug:slug_invest>', views.InvestDeteil, name='InvestDeteilPosts'),
    path('ajaxfavorite/<int:id>/', views.ajaxfavorite, name='ajaxfavorite'),
    path('mapsinvest/', views.InvestPost, {'template':'invest/maps_list.html'}, name='mapsinvest'),



   # path('catalog/<slug:slug_dom>/', views.DetailPosts, name='DetailPosts'),  # new

]