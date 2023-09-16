from django.db import models
from django.contrib.auth.models import User


class Feedback(models.Model):
    """
    Модель обратной связи
    """
    subject = models.CharField(max_length=255, verbose_name='Форма', blank=True)
    phone = models.CharField(max_length=255, verbose_name='Телефон')
    user = models.CharField(max_length=255, verbose_name='Имя', blank=True)
    content = models.TextField(verbose_name='Содержимое письма',  blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
        ordering = ['-time_create']


    def __str__(self):
        return f'{self.subject} - {self.phone} - {self.user}'