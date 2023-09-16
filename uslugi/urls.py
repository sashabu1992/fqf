from django.urls import path
from . import views

urlpatterns = [
       path('uslugi/', views.uslugi, name='uslugi'),
       path('yuridicheskie-uslugi/', views.usl_list, {
        'tipusl' :'usl1',
        'h1': 'ЮРИДИЧЕСКИЕ УСЛУГИ'
        },
        name='yurusl'),
        path('rieltorskie-uslugi/', views.usl_list2, {
        'tipusl' :'usl2',
        'h1': 'РИЭЛТОРСКИЕ УСЛУГИ'
        },
        name='rieltusl'),
]