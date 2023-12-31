# Generated by Django 3.2.19 on 2023-05-04 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20230501_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='content',
            field=models.TextField(blank=True, verbose_name='Содержимое письма'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='subject',
            field=models.CharField(blank=True, max_length=255, verbose_name='Форма'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='user',
            field=models.CharField(blank=True, max_length=255, verbose_name='Имя'),
        ),
    ]
