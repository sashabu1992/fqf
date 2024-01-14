from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django_email_verification import urls as email_urls
from .views import ProfileEditView
from . import views

urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('email/', include(email_urls)),
    path('profile/edit/', ProfileEditView.as_view(), name='profile-edit'),
    path('fav/<int:id>/', views.favourite_add, name='favourite_add'),
    path('fav2/<int:id>/', views.favourite_add2, name='favourite_add2'),
    path('favourites/', views.favourite_list, name='favourite_list'),
]