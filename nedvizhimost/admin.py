from django.contrib import admin
# Register your models here.
# Register your models here.
from .models import Dom, Rajon, GalleryDom, Ulica, Gorod, Komplex
from django.utils.http import urlencode
from django.urls import reverse
from django.utils.safestring import mark_safe
from django import forms

#Предпросмотр фото
class PostImageInlineForm(forms.ModelForm):
    def preview(self, obj):
        return mark_safe(f'<img style="max-width:100px" src="{obj.image.url}">')


class DomGallery(admin.TabularInline):
    model = GalleryDom
    extra = 0



@admin.register(Dom)
class Dom(admin.ModelAdmin):
    search_fields = ("h1", )
    list_display = ('h1', 'preview', 'created', 'is_draft', 'slug')
    fieldsets = (
    	('SEO', {
            'fields': ('title','description', 'slug')
        }), 
        ('Содержимое', {
            'fields': ('h1', 'introtext', 'post')
        }),       
        ('Характеристики объекта', {
            'fields': ('best', 'image_zast', 'preview','category', 'tipcdelki', 'price', 'priceot', 'colkomnat',
                'ploshad', 'gorod', 'rajon','komplex', 'ulica','addres', 'coord')
        }),       
        ('Настройки', {
            'fields': ('created', 'modified', 'published_date', 'is_draft')
        }),

    )
    inlines = [DomGallery]
    readonly_fields = ('created', 'modified', 'preview')
    list_filter = ('is_draft', 'category', 'tipcdelki','best')
    prepopulated_fields = {'slug': ('title',)}

    def preview(self, obj):
        return mark_safe(f'<img style="max-width:100px" src="{obj.image_zast.url}">')


admin.site.register(Gorod)
admin.site.register(Rajon)
admin.site.register(Ulica)
admin.site.register(Komplex)

