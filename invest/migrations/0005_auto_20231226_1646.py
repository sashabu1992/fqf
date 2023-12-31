# Generated by Django 3.2.19 on 2023-12-26 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0004_auto_20231226_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='invest',
            name='present',
            field=models.FileField(blank=True, upload_to='present', verbose_name='Презентация'),
        ),
        migrations.AlterField(
            model_name='invest',
            name='country',
            field=models.CharField(choices=[('not', '---------'), ('russia', 'Россия'), ('oae', 'ОАЭ')], default='russia', max_length=16, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='invest',
            name='deistvie',
            field=models.CharField(choices=[('not', '---------'), ('kupit', 'Купить'), ('prodat', 'Продать')], default='kupit', max_length=16, verbose_name='Действие'),
        ),
        migrations.AlterField(
            model_name='invest',
            name='drugoe',
            field=models.CharField(choices=[('not', '---------'), ('remont', 'с ремонтом'), ('bezremont', 'без ремонта')], default='remont', max_length=16, verbose_name='Другое'),
        ),
        migrations.AlterField(
            model_name='invest',
            name='gotov',
            field=models.CharField(choices=[('not', '---------'), ('gotov', 'строится'), ('sdan', 'сдан')], default='gotov', max_length=16, verbose_name='Готовность'),
        ),
        migrations.AlterField(
            model_name='invest',
            name='tipcdelki',
            field=models.CharField(choices=[('not', '---------'), ('apartament', 'Апартаменты')], default='apartament', max_length=16, verbose_name='Тип'),
        ),
    ]
