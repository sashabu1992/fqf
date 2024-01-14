from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from nedvizhimost.models import Dom
from invest.models import Invest


class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dom = models.ForeignKey(Dom, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'dom', )
        verbose_name = 'Избранное недвижимость'
        verbose_name_plural = 'Избранное недвижимость'

    def __str__(self):
        return f' {self.user.first_name} {self.user.last_name} '


class FavoritesInvest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    invest = models.ForeignKey(Invest, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'invest')
        verbose_name = 'Избранное инвестиции'
        verbose_name_plural = 'Избранное инвестиции'

    def __str__(self):
        return f' {self.user.first_name} {self.user.last_name} '