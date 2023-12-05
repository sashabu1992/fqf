from django.contrib import admin
# Register your models here.
# Register your models here.
from .models import Invest, GalleryDom, TagInvest
from django.utils.http import urlencode
from django.urls import reverse
from django.utils.safestring import mark_safe
from django import forms

#Предпросмотр фото
class PostImageInlineForm(forms.ModelForm):
    def preview(self, obj):
        return mark_safe(f'<img style="max-width:100px" src="{obj.image.url}">')


class GalleryDom(admin.TabularInline):
    model = GalleryDom
    extra = 0

class TagInvest(admin.TabularInline):
    model = TagInvest
    extra = 0


@admin.register(Invest)
class Invest(admin.ModelAdmin):
    search_fields = ("h1", )
    list_display = ('h1', 'created', 'is_draft', 'slug')
    fieldsets = (
    	('SEO', {
            'fields': ('title','description', 'slug')
        }),
        ('Содержимое', {
            'fields': ('h1', 'introtext', 'post')
        }),
        ('Характеристики объекта', {
            'fields': ('deistvie', 'tipcdelki', 'price', 'colkomnat',
                'ploshad', 'adres')
        }),
        ('Настройки', {
            'fields': ('created', 'modified', 'published_date', 'is_draft')
        }),

    )
    inlines = [TagInvest, GalleryDom]
    readonly_fields = ('created', 'modified', )
    list_filter = ('is_draft', 'deistvie', 'tipcdelki',)
    prepopulated_fields = {'slug': ('title',)}



