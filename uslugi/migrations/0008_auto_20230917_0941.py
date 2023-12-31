# Generated by Django 3.2.19 on 2023-09-17 06:41

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('uslugi', '0007_auto_20230916_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='uslugi',
            name='podzag',
            field=models.CharField(blank=True, max_length=3000, verbose_name='Заголовок Блока 1'),
        ),
        migrations.AddField(
            model_name='uslugi',
            name='podzag2',
            field=models.CharField(blank=True, max_length=3000, verbose_name='Заголовок Блока 2'),
        ),
        migrations.AddField(
            model_name='uslugi',
            name='podzag3',
            field=models.CharField(blank=True, max_length=3000, verbose_name='Заголовок Блока 3'),
        ),
        migrations.AddField(
            model_name='uslugi',
            name='post2',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, verbose_name='Блок 2'),
        ),
        migrations.AddField(
            model_name='uslugi',
            name='post3',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, verbose_name='Блок 3'),
        ),
        migrations.AlterField(
            model_name='uslugi',
            name='post',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, verbose_name='Блок 1'),
        ),
    ]
