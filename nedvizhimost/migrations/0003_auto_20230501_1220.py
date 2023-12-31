# Generated by Django 3.2.18 on 2023-05-01 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nedvizhimost', '0002_auto_20230427_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dom',
            name='category',
            field=models.CharField(choices=[('kvartira', 'Квартиры'), ('komerch', 'Комерческая недвижимость'), ('zagorod', 'Загородные дома'), ('garazh', 'Гаражи'), ('zemuch', 'Земельные участки'), ('newstroi', 'Новостройки')], default='kvartira', max_length=16, verbose_name='Категория недвижимости'),
        ),
        migrations.AlterField(
            model_name='dom',
            name='tipcdelki',
            field=models.CharField(choices=[('kupit', 'Купить'), ('prodat', 'Продать'), ('snat', 'Снять'), ('cdat', 'Сдать'), ('arenda', 'Аренда')], default='kupit', max_length=16, verbose_name='Тип сделки'),
        ),
    ]
