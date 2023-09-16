# Generated by Django 3.2.19 on 2023-09-16 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uslugi', '0005_auto_20230916_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='uslugi',
            name='created',
            field=models.DateField(blank=True, default='2023-04-28', verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='uslugi',
            name='is_draft',
            field=models.BooleanField(default=True, verbose_name='Опубликован'),
        ),
        migrations.AddField(
            model_name='uslugi',
            name='modified',
            field=models.DateField(blank=True, default='2023-04-28', verbose_name='Дата изменения'),
        ),
        migrations.AddField(
            model_name='uslugi',
            name='published_date',
            field=models.DateTimeField(blank=True, default='2023-04-28', null=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='uslugi',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True, verbose_name='URl'),
        ),
        migrations.AlterField(
            model_name='uslugi',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок Title'),
        ),
    ]