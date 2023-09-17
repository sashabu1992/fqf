from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.
import uuid
import os
from slugify import slugify
from django.urls import reverse
from django.core.exceptions import ValidationError

class PriceUslugi(models.Model):
    zag = models.TextField(max_length=3000, verbose_name="Заголовок", blank=True)
    post = CKEditor5Field( verbose_name="Контент", blank=True, config_name='extends')
    class Meta:
        ordering = ('id',)
        verbose_name = ('Прайс на услуги')
        verbose_name_plural = ('Прайс на услуги')
    
    def __str__(self):
        """Return title and username."""
        return str(self.zag) 

TIPUSLUGI_CHOISE= (
    ('usl1','Юридические услуги'),
    ('usl2', 'Риэлторские услуги')
)
CATUSLUGI_CHOISE= (
    ('doc','Оформление документов'),
    ('dogovor', 'Договоры'),
    ('soprsdel','Сопровождение сделок'),
    ('oformldoc','Оформление наследства'),
    ('zhi1','Жилые помещения'),
    ('zhi2','Загородная недвижимость'),
    ('zhi3','Нежилые помещения'),
    ('zhi4','коммерческая недвижимость')
)

def get_file_image_zast_usl(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('img/image_zast_usl/', filename)

def get_file_image_zast_usl_form(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('img/image_zast_usl_form/', filename)


def increment_slug(slug, obj):
    """
    Добавляет числовой суффикс к slug, если он уже существует в базе данных.
    Например, если slug="test", а в базе данных уже есть запись с таким slug,
    то функция вернет "test-1". Если "test-1" тоже уже существует, то вернет "test-2" и т.д.
    """
    original_slug = slug
    counter = 1
    while Uslugi.objects.filter(slug=slug).exclude(id=obj.id).exists():
        slug = '{}-{}'.format(original_slug, counter)
        counter += 1
    return slug if original_slug == slug else slug + '-1'

class Uslugi(models.Model):
    slug = models.SlugField(max_length=255, blank=True, unique=True,  verbose_name="URl")
    """СЕО натсрйоки"""
    title = models.CharField(max_length=255, verbose_name="Заголовок Title")
    description = models.CharField(max_length=350, verbose_name="Заголовок Description", blank=True)
    """Основные данные """
    zag = models.CharField(max_length=3000, verbose_name="Заголовок", blank=True)
    tipusl = models.CharField(max_length=16, choices=TIPUSLUGI_CHOISE, default='usl1', verbose_name="Тип услуги")
    tipcdelki = models.CharField(max_length=16, choices=CATUSLUGI_CHOISE, default='doc', verbose_name="Категория услуги")
    image_zast = models.ImageField(upload_to=get_file_image_zast_usl, verbose_name="Заставка услуги", blank=False)
    image_zast_verh = models.ImageField(upload_to=get_file_image_zast_usl_form, verbose_name="Заставка услуги в форму", blank=False)
    podzag = models.CharField(max_length=3000, verbose_name="Заголовок Блока 1", blank=True)
    post = CKEditor5Field( verbose_name="Блок 1", blank=True, config_name='extends')
    podzag2 = models.CharField(max_length=3000, verbose_name="Заголовок Блока 2", blank=True)
    post2 = CKEditor5Field(verbose_name="Блок 2", blank=True, config_name='extends')
    podzag3 = models.CharField(max_length=3000, verbose_name="Заголовок Блока 3", blank=True)
    post3 = CKEditor5Field(verbose_name="Блок 3", blank=True, config_name='extends')
    best = models.BooleanField(default=False, verbose_name="Лучшее предложение")
    price = models.IntegerField( default='0', verbose_name="Цена")
    published_date = models.DateTimeField(blank=True, null=True, verbose_name="Дата публикации")
    created = models.DateField(auto_now=True, blank=True, verbose_name="Дата создания")
    modified = models.DateField( blank=True, auto_now=True, verbose_name="Дата изменения")
    is_draft = models.BooleanField(default=True, verbose_name="Опубликован")


    class Meta:
        ordering = ('id',)
        verbose_name = ('Услуги')
        verbose_name_plural = ('Услуги')

    def get_absolute_url(self):
        return reverse('DetailUslug', kwargs={'slug_uslug': self.slug}) # new


    def clean(self):
        if not self.slug:
            self.slug = slugify(self.title)
        while Uslugi.objects.filter(slug=self.slug).exclude(id=self.id).exists():
            self.slug = increment_slug(self.slug, self)
        super(Uslugi, self).clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Uslugi, self).save(*args, **kwargs)

    def __str__(self):
        """Return title and username."""
        return str(self.title)


# Модель вопрос ответ
class VoprosOtvet(models.Model):
    usluga = models.ForeignKey(Uslugi, verbose_name='Услуга', on_delete=models.CASCADE)
    vopros = models.TextField(max_length=3000, verbose_name="Вопрос", blank=True)
    otvet = CKEditor5Field(max_length=10000, verbose_name="Ответ", blank=True, config_name='extends')

    class Meta:
        ordering = ('id',)
        verbose_name = ('Вопрос - Ответ для услуг')
        verbose_name_plural = ('Вопрос - Ответ для услуг')

    def __str__(self):
        """Return title and username."""
        return str(self.vopros)