# Generated by Django 3.2.19 on 2023-09-17 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uslugi', '0010_auto_20230917_1002'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='voprosotvet',
            options={'ordering': ('id',), 'verbose_name': 'Вопрос - Ответ для услуг', 'verbose_name_plural': 'Вопрос - Ответ для услуг'},
        ),
    ]
