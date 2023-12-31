# Generated by Django 3.2.18 on 2023-04-27 11:13

from django.db import migrations, models
import django.db.models.deletion
import django_ckeditor_5.fields
import nedvizhimost.models


class Migration(migrations.Migration):

    dependencies = [
        ('nedvizhimost', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gorod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Komplex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Жилой комплекс')),
            ],
            options={
                'verbose_name': 'Жилой комплекс',
                'verbose_name_plural': 'Жилые комплексы',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Rajon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Район')),
            ],
            options={
                'verbose_name': 'Районы',
                'verbose_name_plural': 'Районы',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Ulica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Улица')),
            ],
            options={
                'verbose_name': 'Улица',
                'verbose_name_plural': 'Улицы',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='dom',
            name='addres',
            field=models.CharField(blank=True, max_length=855, null=True, verbose_name='Адресс'),
        ),
        migrations.AddField(
            model_name='dom',
            name='best',
            field=models.BooleanField(default=False, verbose_name='Лучшее предложение'),
        ),
        migrations.AddField(
            model_name='dom',
            name='category',
            field=models.CharField(choices=[('kvartira', 'Квартиры'), ('komerch', 'Комерческая недвижимость'), ('zagorod', 'Загородные дома'), ('garazh', 'Гаражи'), ('zemuch', 'Земельные участки'), ('arenda', 'Аренда')], default='kvartira', max_length=16, verbose_name='Категория недвижимости'),
        ),
        migrations.AddField(
            model_name='dom',
            name='coord',
            field=models.CharField(default=1, max_length=255, verbose_name='Координаты (56.033470, 38.121869)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dom',
            name='ploshad',
            field=models.IntegerField(default='0', verbose_name='Площадь'),
        ),
        migrations.AddField(
            model_name='dom',
            name='price',
            field=models.IntegerField(default='0', verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='dom',
            name='tipcdelki',
            field=models.CharField(choices=[('kupit', 'Купить'), ('prodat', 'Продать'), ('snat', 'Снять'), ('cdat', 'Сдать')], default='kupit', max_length=16, verbose_name='Тип сделки'),
        ),
        migrations.AlterField(
            model_name='dom',
            name='image_zast',
            field=models.ImageField(upload_to=nedvizhimost.models.get_file_image_zast, verbose_name='Заставка объекта'),
        ),
        migrations.AlterField(
            model_name='dom',
            name='post',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, verbose_name='Содержание'),
        ),
        migrations.CreateModel(
            name='GalleryDom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=nedvizhimost.models.get_file_image_foto, verbose_name='Фото объекта')),
                ('alt', models.CharField(blank=True, max_length=1000, verbose_name='Тег ALT')),
                ('dom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nedvizhimost.dom', verbose_name='Объект недвижимости')),
            ],
        ),
        migrations.AddField(
            model_name='dom',
            name='gorod',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='nedvizhimost.gorod', verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='dom',
            name='komplex',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='nedvizhimost.komplex', verbose_name='Жилой комплекс'),
        ),
        migrations.AddField(
            model_name='dom',
            name='rajon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='nedvizhimost.rajon', verbose_name='Район'),
        ),
        migrations.AddField(
            model_name='dom',
            name='ulica',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='nedvizhimost.ulica', verbose_name='Улица'),
        ),
    ]
