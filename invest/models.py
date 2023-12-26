from django.db import models
from slugify import slugify

from django.urls import reverse
import uuid
import os
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import User

# Create your models here.


DEISTVIE_CHOISE= (
    ('not','---------'),
    ('kupit','Купить'),
    ('prodat', 'Продать')
)
TIP_CHOISE= (
    ('not','---------'),
    ('apartament','Апартаменты'),
)
GOTOV= (
    ('not','---------'),
    ('gotov','строится'),
    ('sdan','сдан'),
)
DRUGOE= (
    ('not','---------'),
    ('remont','с ремонтом'),
    ('bezremont','без ремонта'),
)
COUNTRY= (
    ('not','---------'),
    ('russia','Россия'),
    ('oae','ОАЭ'),
)
COL_KOMNAT= (
    ('not','---------'),
    ('stud','Студия'),
    ('1k', '1'),
    ('2k','2'),
    ('3k','3'),
    ('4k','4+'),
)



def increment_slug(slug, obj):
    """
    Добавляет числовой суффикс к slug, если он уже существует в базе данных.
    Например, если slug="test", а в базе данных уже есть запись с таким slug,
    то функция вернет "test-1". Если "test-1" тоже уже существует, то вернет "test-2" и т.д.
    """
    original_slug = slug
    counter = 1
    while Invest.objects.filter(slug=slug).exclude(id=obj.id).exists():
        slug = '{}-{}'.format(original_slug, counter)
        counter += 1
    return slug if original_slug == slug else slug + '-1'


class Invest(models.Model):
    slug = models.SlugField(max_length=255, blank=True, unique=True, verbose_name="URl")
    """СЕО натсрйоки"""
    title = models.CharField(max_length=255, verbose_name="Заголовок Title")
    description = models.CharField(max_length=350, verbose_name="Заголовок Description", blank=True)

    """Основные данные """
    h1 = models.CharField(max_length=255, verbose_name="Заголовок H1")
    introtext = models.TextField(max_length=1000, verbose_name="Краткое описание(в карточку)", blank=True)
    post = CKEditor5Field(verbose_name="Содержание", blank=True, config_name='extends')
    infrastr = CKEditor5Field(verbose_name="Инфраструктура", blank=True, config_name='extends')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name="Дата публикации")
    created = models.DateField(auto_now_add=True, blank=True, verbose_name="Дата создания")
    modified = models.DateField(auto_now=True, verbose_name="Дата изменения")
    is_draft = models.BooleanField(default=True, verbose_name="Опубликован")

    """Основные характеристики"""
    deistvie = models.CharField(max_length=16, choices=DEISTVIE_CHOISE, default='kupit',
                                verbose_name="Действие")
    tipcdelki = models.CharField(max_length=16, choices=TIP_CHOISE, default='apartament', verbose_name="Тип")
    colkomnat = models.CharField(max_length=16, choices=COL_KOMNAT, default='not', verbose_name="Кол-во комнат")
    ploshad = models.IntegerField(default='0', verbose_name="Площадь")
    price = models.IntegerField(default='0', verbose_name="Цена")
    adres = models.CharField(max_length=555, blank=True, verbose_name="Адрес")
    gotov = models.CharField(max_length=16, choices=GOTOV, default='gotov',
                                verbose_name="Готовность")
    drugoe = models.CharField(max_length=16, choices=DRUGOE, default='remont',
                                verbose_name="Другое")
    country = models.CharField(max_length=16, choices=COUNTRY, default='russia',
                              verbose_name="Страна")
    present = models.FileField(upload_to="present", blank=True, verbose_name="Презентация")

    class Meta:
        ordering = ('title',)
        verbose_name = ('Инвестиции')
        verbose_name_plural = ('Инвестиции')

    def __str__(self):
        """Return title and username."""
        return str(self.h1)

    def get_absolute_url(self):
        return reverse('InvestDeteilPosts', kwargs={'slug_invest': self.slug})  # new

    def clean(self):
        if not self.slug:
            self.slug = slugify(self.title)
        while Invest.objects.filter(slug=self.slug).exclude(id=self.id).exists():
            self.slug = increment_slug(self.slug, self)
        super(Invest, self).clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Invest, self).save(*args, **kwargs)


def get_file_image_foto(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('img/image_invest/', filename)

#Модель Фтогалерреи
class GalleryDom(models.Model):
    invest = models.ForeignKey(Invest, verbose_name='Объект недвижимости', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_file_image_foto, verbose_name="Фото объекта")
    alt  = models.CharField(max_length=1000, verbose_name="Тег ALT", blank=True)

class TagInvest(models.Model):
    invest = models.ForeignKey(Invest, verbose_name='Объект недвижимости', on_delete=models.CASCADE)
    tag  = models.CharField(max_length=1000, verbose_name="Тег", blank=True)