from django.contrib import admin
from .models import PriceUslugi, Uslugi, VoprosOtvet
from django import forms

# Register your models here.
admin.site.register(PriceUslugi)


@admin.register(VoprosOtvet)
class VoprosOtvet(admin.ModelAdmin):
    search_fields = ('vopros',  )
    list_display = ('usluga', 'vopros', 'otvet', )
    list_filter = ('usluga',  )




@admin.register(Uslugi)
class Uslugi(admin.ModelAdmin):
    search_fields = ('zag',  )
    list_display = ('zag', 'slug', 'tipusl', 'tipcdelki', 'price', 'best', 'is_draft')
    list_filter = ('tipusl', 'tipcdelki', 'best', 'is_draft')
    fieldsets = (
        ('SEO', {
            'fields': ('title', 'description', 'slug')
        }),
        ('Основные данные', {
            'fields': ('zag', 'tipusl', 'tipcdelki', 'image_zast', 'image_zast_verh', 'podzag','post','podzag2','post2','podzag3','post3', 'price' )
        }),
        ('Настройки', {
            'fields': ('best', 'created', 'modified', 'published_date', 'is_draft')
        }),
    )
    readonly_fields = ('created', 'modified')



