from django.db import models
from slugify import slugify

from django.urls import reverse
import uuid
import os
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import User

CATEGORY_CHOISE= (
    ('kvartira','Квартиры'),
    ('komerch', 'Коммерческая недвижимость'),
    ('zagorod','Загородные дома'),
    ('garazh','Гаражи'),
    ('zemuch','Земельные участки'),
    ('newstroi','Новостройки'),
)
TIPCDELKI_CHOISE= (
    ('kupit','Купить'),
    ('prodat', 'Продать'),
    ('snat','Снять'),
    ('cdat','Сдать')
)
COL_KOMNAT= (
    ('not','---------'),
    ('stud','Студия'),
    ('1k', '1'),
    ('2k','2'),
    ('3k','3'),
    ('4k','4+'),
)

def get_file_image_zast(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('img/image_zast/', filename)

def increment_slug(slug, obj):
    """
    Добавляет числовой суффикс к slug, если он уже существует в базе данных.
    Например, если slug="test", а в базе данных уже есть запись с таким slug,
    то функция вернет "test-1". Если "test-1" тоже уже существует, то вернет "test-2" и т.д.
    """
    original_slug = slug
    counter = 1
    while Dom.objects.filter(slug=slug).exclude(id=obj.id).exists():
        slug = '{}-{}'.format(original_slug, counter)
        counter += 1
    return slug if original_slug == slug else slug + '-1'

class Dom(models.Model):
    slug = models.SlugField(max_length=255, blank=True, unique=True, verbose_name="URl")
    """СЕО натсрйоки"""
    title = models.CharField(max_length=255, verbose_name="Заголовок Title")
    description = models.CharField(max_length=350, verbose_name="Заголовок Description", blank=True)
    
    """Основные данные """
    h1 = models.CharField(max_length=255, verbose_name="Заголовок H1")
    image_zast = models.ImageField(upload_to=get_file_image_zast, verbose_name="Заставка объекта", blank=False)
    post = CKEditor5Field( verbose_name="Содержание", blank=True, config_name='extends')
    introtext = models.TextField(max_length=1000, verbose_name="Краткое описание", blank=True)
    published_date = models.DateTimeField(blank=True, null=True,  verbose_name="Дата публикации")
    created = models.DateField(auto_now_add=True, blank=True, verbose_name="Дата создания")
    modified = models.DateField(auto_now=True, verbose_name="Дата изменения")
    is_draft = models.BooleanField(default=True, verbose_name="Опубликован")

    """Основные характеристики"""
    best = models.BooleanField(default=False, verbose_name="Лучшее предложение")
    category = models.CharField(max_length=16, choices=CATEGORY_CHOISE, default='kvartira', verbose_name="Категория недвижимости")
    tipcdelki = models.CharField(max_length=16, choices=TIPCDELKI_CHOISE, default='kupit', verbose_name="Тип сделки")
    price = models.IntegerField( default='0', verbose_name="Цена")
    priceot = models.BooleanField(default=False, verbose_name="Цена от")
    ploshad = models.IntegerField( default='0', verbose_name="Площадь")
    colkomnat = models.CharField(max_length=16, choices=COL_KOMNAT, default='not', verbose_name="Кол-во комнат")
    rajon = models.ForeignKey('Rajon', on_delete=models.PROTECT, null=True, blank=True, verbose_name="Район")
    gorod = models.ForeignKey('Gorod', on_delete=models.PROTECT, null=True, blank=True, verbose_name="Город")
    ulica = models.ForeignKey('Ulica', on_delete=models.PROTECT, null=True, blank=True, verbose_name="Улица")
    komplex = models.ForeignKey('Komplex', on_delete=models.PROTECT, null=True, blank=True, verbose_name="Жилой комплекс")
    addres = models.CharField(max_length=855, verbose_name="Адресс", blank=True, null=True)
    coord = models.CharField(max_length=255, verbose_name="Координаты (56.033470, 38.121869)")
    """избранное """
    favorit = models.ManyToManyField(User, related_name='favorite', verbose_name="Избранное", default=None, blank=True)

    class Meta:
        ordering = ('title',)
        verbose_name = ('Недвижимость')
        verbose_name_plural = ('Недвижимость')

    def __str__(self):
        """Return title and username."""
        return str(self.h1) 

    def get_absolute_url(self):
        return reverse('DetailPosts', kwargs={'slug_dom': self.slug}) # new
    def clean(self):
        if not self.slug:
            self.slug = slugify(self.title)
        while Dom.objects.filter(slug=self.slug).exclude(id=self.id).exists():
            self.slug = increment_slug(self.slug, self)
        super(Dom, self).clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Dom, self).save(*args, **kwargs)



def get_file_image_foto(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('img/image_object/', filename)

#Модель Фтогалерреи
class GalleryDom(models.Model):
    dom = models.ForeignKey(Dom, verbose_name='Объект недвижимости', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_file_image_foto, verbose_name="Фото объекта")
    alt  = models.CharField(max_length=1000, verbose_name="Тег ALT", blank=True)




#Модель Районов
class Rajon(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Район")
    
    class Meta:
        ordering = ('name',)
        verbose_name = ('Районы')
        verbose_name_plural = ('Районы')
    
    def __str__(self):
        """Return title and username."""
        return str(self.name) 


#Модель городов
class Gorod(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Город")
    
    class Meta:
        ordering = ('name',)
        verbose_name = ('Город')
        verbose_name_plural = ('Города')
    
    def __str__(self):
        """Return title and username."""
        return str(self.name) 

#Модель улиц
class Ulica(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Улица")
    
    class Meta:
        ordering = ('name',)
        verbose_name = ('Улица')
        verbose_name_plural = ('Улицы')
    
    def __str__(self):
        """Return title and username."""
        return str(self.name) 


#Модель жилой комплекс
class Komplex(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Жилой комплекс")
    
    class Meta:
        ordering = ('name',)
        verbose_name = ('Жилой комплекс')
        verbose_name_plural = ('Жилые комплексы')
    
    def __str__(self):
        """Return title and username."""
        return str(self.name) 