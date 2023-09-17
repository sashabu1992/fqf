from django.contrib import admin
# Register your models here.
# Register your models here.
from .models import WebsiteSettings, VoprosOtvet, Baher, Partner, BankPartner, WebsiteContent, Revius_klient, OficeImg, PlusVam
from django.utils.http import urlencode
from django.urls import reverse
from django.utils.safestring import mark_safe
from django import forms




@admin.register(BankPartner)
class BankPartner(admin.ModelAdmin):
    list_display = ( 'preview', 'alt' )
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img style="max-width:200px" src="{obj.image_zast.url}">')

@admin.register(Partner)
class Partner(admin.ModelAdmin):
    list_display = ( 'preview', 'alt' )
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img style="max-width:200px" src="{obj.image_zast.url}">')

@admin.register(OficeImg)
class OficeImg(admin.ModelAdmin):
    list_display = ( 'preview', 'alt' )
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img style="max-width:200px" src="{obj.image.url}">')

@admin.register(Baher)
class Baher(admin.ModelAdmin):
    list_display = ( 'preview', 'alt' )
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img style="max-width:200px" src="{obj.image_zast.url}">')

admin.site.register(VoprosOtvet)
admin.site.register(WebsiteSettings)
admin.site.register(Revius_klient)
admin.site.register(PlusVam)



@admin.register(WebsiteContent)
class WebsiteContent(admin.ModelAdmin):
    list_display = ('language', )
    fieldsets = (
        ('Язык', {
            'fields': ('language',)
        }), 
        ('БАНКИ - ПАРТНЕРЫ', {
            'fields': ('text_bankpartner',)
        }), 
        ('БОНУСЫ ОТ КОМПАНИЙ', {
            'fields': ('text_bonus',)
        }),   
        ('Услуги', {
            'fields': ('text_uslugi',)
        }),   
        ('Юридические услуги', {
            'fields': ('preview2', 'image_yuruslug', 'text_yuruslug')
        }),
        ('Риэлторские услуги', {
            'fields': ('preview3', 'image_rieltuslug', 'text_rieltuslug')
        }),  
        ('О НАС', {
            'fields': ('preview', 'image_onas', 'text_onas_glav', 'text_onas')
        }),       
        ('Политика конфидициальности', {
            'fields': ('text_politic',)
        })

    )
    readonly_fields = ('preview','preview2','preview3')

    def preview(self, obj):
        return mark_safe(f'<img style="max-width:200px" src="{obj.image_onas.url}">')

    def preview2(self, obj):
        return mark_safe(f'<img style="max-width:200px" src="{obj.image_yuruslug.url}">')

    def preview3(self, obj):
        return mark_safe(f'<img style="max-width:200px" src="{obj.image_rieltuslug.url}">')

