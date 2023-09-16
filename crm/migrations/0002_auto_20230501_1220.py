# Generated by Django 3.2.18 on 2023-05-01 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='ip_address',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='phone',
            field=models.CharField(max_length=255, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='user',
            field=models.CharField(max_length=255, verbose_name='Имя'),
        ),
        migrations.AlterModelTable(
            name='feedback',
            table=None,
        ),
    ]
