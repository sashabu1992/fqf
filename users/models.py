from django.db import models
from django.contrib.auth.models import User
import uuid
import os
from django.dispatch import receiver
from django.db.models.signals import post_save
from nedvizhimost.models import Dom
def get_file_image_user(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('img/user/', filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Профиль пользователя',)
    phone = models.CharField(max_length=255, verbose_name="Телефон", blank=True)
    bio = models.TextField(max_length=500, verbose_name='Информация о себе', blank=True)
    avatar = models.ImageField(
        verbose_name='Аватар профиля',
        blank=True,
        upload_to=get_file_image_user,
    )
    date_birthday = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    favorites = models.ManyToManyField(Dom)

    class Meta:
        verbose_name = ('Профиль')
        verbose_name_plural = ('Профили')

    def __str__(self):
        return f'Профиль {self.user.username} - {self.user.first_name} {self.user.last_name} '

    @property
    def get_avatar(self):
        """
        Получение аватара при отсутствии загруженного
        """
        if not self.avatar:
            return f'https://ui-avatars.com/api/?size=128&background=random&name={self.user.username}'
        return self.avatar.url

    @property
    def get_age(self):
        """
        Вычисление возраста пользователя
        """
        return (date.today() - self.date_birthday) // timedelta(days=365.2425)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Сигнал создания профиля пользователя
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Сигнал пересохранения профиля пользователя
    """
    instance.profile.save()