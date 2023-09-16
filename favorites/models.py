from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from nedvizhimost.models import Dom


class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dom = models.ForeignKey(Dom, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'dom')
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'

    def __str__(self):
        return f' {self.user.first_name} {self.user.last_name} '