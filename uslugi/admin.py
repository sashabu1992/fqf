from django.contrib import admin
from .models import PriceUslugi, Uslugi
from django import forms


# Register your models here.
admin.site.register(PriceUslugi)



@admin.register(Uslugi)
class Uslugi(admin.ModelAdmin):
    search_fields = ("h1", )
    list_display = ('zag', 'tipusl', 'tipcdelki', 'price', 'best')
    list_filter = ('tipusl', 'tipcdelki', 'best')

