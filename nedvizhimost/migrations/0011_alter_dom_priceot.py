# Generated by Django 3.2.19 on 2023-09-16 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nedvizhimost', '0010_dom_priceot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dom',
            name='priceot',
            field=models.BooleanField(default=False, verbose_name='Цена от'),
        ),
    ]
