from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.
import uuid
import os

class PriceUslugi(models.Model):
    zag = models.CharField(max_length=3000, verbose_name="Заголовок", blank=True)
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


class Uslugi(models.Model):
    zag = models.CharField(max_length=3000, verbose_name="Заголовок", blank=True)
    tipusl = models.CharField(max_length=16, choices=TIPUSLUGI_CHOISE, default='usl1', verbose_name="Тип услуги")
    tipcdelki = models.CharField(max_length=16, choices=CATUSLUGI_CHOISE, default='doc', verbose_name="Категория услуги")
    image_zast = models.ImageField(upload_to=get_file_image_zast_usl, verbose_name="Заставка услуги", blank=False)
    image_zast_verh = models.ImageField(upload_to=get_file_image_zast_usl_form, verbose_name="Заставка услуги в форму", blank=False)
    post = CKEditor5Field( verbose_name="Контент", blank=True, config_name='extends')
    best = models.BooleanField(default=False, verbose_name="Лучшее предложение")
    price = models.IntegerField( default='0', verbose_name="Цена")


    class Meta:
        ordering = ('id',)
        verbose_name = ('Услуги')
        verbose_name_plural = ('Услуги')
    
    def __str__(self):
        """Return title and username."""
        return str(self.zag) 