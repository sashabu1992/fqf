# Generated by Django 3.2.19 on 2023-12-05 15:15

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('websitesetting', '0011_plusvam_imagemob'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='text',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, verbose_name='Текст '),
        ),
        migrations.AddField(
            model_name='partner',
            name='zag',
            field=models.CharField(blank=True, max_length=250, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='plusvam',
            name='text',
            field=models.TextField(max_length=6000, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='plusvam',
            name='zag',
            field=models.CharField(max_length=250, verbose_name='Заголовок'),
        ),
    ]
