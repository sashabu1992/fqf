from django.db import models

# Create your models here.
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext as _
from django.urls import reverse
import uuid
import os
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django_ckeditor_5.fields import CKEditor5Field
from django.core.validators import MaxValueValidator, MinValueValidator


class WebsiteSettings(models.Model):
    language = models.CharField(max_length=16, unique=True, choices=settings.LANGUAGES, verbose_name=_('Язык'))
    name_site = models.CharField(max_length=100, blank=True, verbose_name=_('Название сайта'))
    #Контактные данные
    phone1 = models.CharField(max_length=25, blank=True, verbose_name=_('Основной телефон'))
    phone2 = models.CharField(max_length=25, blank=True, verbose_name=_('Дополнительный телефон'))
    email = models.CharField(max_length=200, blank=True, verbose_name=_('Email'))
    addr = models.TextField(max_length=500, blank=True, verbose_name=_('Адрес'))
    maps = models.TextField(max_length=5000, blank=True, verbose_name=_('Код карты'))
    inn = models.CharField(max_length=20, blank=True, verbose_name=_('ИНН'))
    kpp = models.CharField(max_length=20, blank=True, verbose_name=_('КПП'))
    ogrn = models.CharField(max_length=20, blank=True, verbose_name=_('ОГРН'))
    #Соцсети и мессенджеры:
    vk = models.CharField(max_length=1000, blank=True, verbose_name=_('Вконтакте'))
    teleg = models.CharField(max_length=1000, blank=True, verbose_name=_('Телеграм'))
    inst = models.CharField(max_length=1000, blank=True, verbose_name=_('Инстаграм'))


    class Meta:
        verbose_name = _('Системные настройки')
        verbose_name_plural = _('Системные настройки')
        ordering = ['language']

    def __str__(self):
        """Return title and username."""
        return str(self.language) 


def get_file_image_flat(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('img/image_flatepage/', filename)

class WebsiteContent(models.Model):
    language = models.CharField(max_length=16, unique=True, choices=settings.LANGUAGES, verbose_name=_('Язык'))
    #политика конфидициальности
    text_politic = CKEditor5Field( verbose_name="Текст политики конфидициальности ", blank=True, config_name='extends')
    #БАНКИ - ПАРТНЕРЫ
    text_bankpartner = CKEditor5Field( verbose_name="Описание блока БАНКИ - ПАРТНЕРЫ", blank=True, config_name='extends')
    #БОНУСЫ ОТ КОМПАНИЙ
    text_bonus = CKEditor5Field( verbose_name="Описание блока БОНУСЫ ОТ КОМПАНИЙ", blank=True, config_name='extends')
    #Блок О НАС
    image_onas = models.ImageField(upload_to=get_file_image_flat, verbose_name="Картинка в блок на главную", blank=True, null=True)
    text_onas_glav = CKEditor5Field( verbose_name="Текст на главную", blank=True, config_name='extends')
    text_onas = CKEditor5Field( verbose_name="Текст на страницу о нас", blank=True, config_name='extends')
    #Услуги
    text_uslugi = CKEditor5Field( verbose_name="Текст на страницу услуги", blank=True, config_name='extends')
    #Блок Юридические услуги
    image_yuruslug = models.ImageField(upload_to=get_file_image_flat, verbose_name="Картинка Юр.услуг", blank=True, null=True)
    text_yuruslug = CKEditor5Field( verbose_name="Текст Юр.услуг", blank=True, config_name='extends')
    #Блок Юридические услуги
    image_rieltuslug = models.ImageField(upload_to=get_file_image_flat, verbose_name="Картинка Риэлт.услуг", blank=True, null=True)
    text_rieltuslug = CKEditor5Field( verbose_name="Текст Риэлт.услуг", blank=True, config_name='extends')
    

    class Meta:
        verbose_name = _('Статический контент')
        verbose_name_plural = _('Статический контент')
        ordering = ['language']

    def __str__(self):
        """Return title and username."""
        return str(self.language) 


#Модель вопрос ответ
class VoprosOtvet(models.Model):
    vopros = models.TextField(max_length=3000, verbose_name="Вопрос", blank=True)
    otvet  = CKEditor5Field(max_length=10000, verbose_name="Ответ", blank=True, config_name='extends')
    class Meta:
        ordering = ('id',)
        verbose_name = ('Вопрос - Ответ')
        verbose_name_plural = ('Вопрос - Ответ')
    
    def __str__(self):
        """Return title and username."""
        return str(self.vopros) 


def get_file_image_baner(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('img/baher/', filename)

#Модель Банеров на главную
class Baher(models.Model):
    image_zast = models.ImageField(upload_to=get_file_image_baner, verbose_name="Картинка", blank=False)
    url = models.CharField(max_length=3000, verbose_name="Ссылка", blank=True)
    alt  = models.CharField(max_length=1000, verbose_name="Тег ALT", blank=True)
    class Meta:
        ordering = ('id',)
        verbose_name = ('Банеры на главную')
        verbose_name_plural = ('Банеры на главную')
    
    def __str__(self):
        """Return title and username."""
        return str(self.image_zast) 

def get_file_image_partner(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('img/partner/', filename)

#Модель партнеров
class Partner(models.Model):
    image_zast = models.ImageField(upload_to=get_file_image_partner, verbose_name="Лого", blank=False)
    alt  = models.CharField(max_length=1000, verbose_name="Тег ALT", blank=True)
    zag = models.CharField(max_length=250, blank=True, verbose_name=_('Заголовок'))
    text = CKEditor5Field(verbose_name="Текст ", blank=True, config_name='extends')
    class Meta:
        ordering = ('id',)
        verbose_name = ('Наши Партнеры')
        verbose_name_plural = ('Наши Партнеры')
    
    def __str__(self):
        """Return title and username."""
        return str(self.image_zast) 

#Модель банки пратнеры
class BankPartner(models.Model):
    image_zast = models.ImageField(upload_to=get_file_image_partner, verbose_name="Лого", blank=False)
    alt  = models.CharField(max_length=1000, verbose_name="Тег ALT", blank=True)
    class Meta:
        ordering = ('id',)
        verbose_name = ('Банки Партнеры')
        verbose_name_plural = ('Банки Партнеры')
    
    def __str__(self):
        """Return title and username."""
        return str(self.image_zast)

    # Отзывы клиентов
class Revius_klient(models.Model):
    name = models.CharField(max_length=250, blank=True, verbose_name=_('Имя'))
    text = models.TextField(max_length=6000, verbose_name="Отзыв", blank=True)
    kolstar = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ],
        blank=False,
        null=False
    )
    class Meta:
        ordering = ('id',)
        verbose_name = ('Отзывы клиентов')
        verbose_name_plural = ('Отзывы клиентов')

    def __str__(self):
        """Return title and username."""
        return str(self.name)

#В офисе – как дома
def get_file_image_office(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('img/office/', filename)

class OficeImg(models.Model):
    image = models.ImageField(upload_to=get_file_image_office, verbose_name="Фото", blank=False)
    alt = models.CharField(max_length=1000, verbose_name="Тег ALT", blank=True)

    class Meta:
        ordering = ('id',)
        verbose_name = ('В офисе – как дома')
        verbose_name_plural = ('В офисе – как дома')

    def __str__(self):
        """Return title and username."""
        return str(self.image)

def get_file_image_plus(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('img/plus/', filename)
def get_file_image_plusmob(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('img/plus/mob/', filename)

class PlusVam(models.Model):
    image = models.ImageField(upload_to=get_file_image_plus, verbose_name="Фото", blank=False)
    imagemob = models.ImageField(upload_to=get_file_image_plusmob, verbose_name="Фото в мобилку", blank=False)
    zag = models.CharField(max_length=250, blank=False, verbose_name=_('Заголовок'))
    text = models.TextField(max_length=6000, blank=False, verbose_name="Текст")

    class Meta:
        ordering = ('id',)
        verbose_name = ('Преимущества для вас')
        verbose_name_plural = ('Преимущества для вас')

    def __str__(self):
        """Return title and username."""
        return str(self.zag)