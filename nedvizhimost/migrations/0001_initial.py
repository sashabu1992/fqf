# Generated by Django 3.2.18 on 2023-03-16 10:46

from django.db import migrations, models
import nedvizhimost.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок Title')),
                ('description', models.CharField(blank=True, max_length=350, verbose_name='Заголовок Description')),
                ('h1', models.CharField(max_length=255, verbose_name='Заголовок H1')),
                ('image_zast', models.ImageField(blank=True, upload_to=nedvizhimost.models.get_file_image_zast, verbose_name='Заставка категории')),
                ('post', models.TextField(blank=True, verbose_name='Содержание')),
                ('introtext', models.TextField(blank=True, max_length=1000, verbose_name='Краткое описание')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('modified', models.DateField(auto_now=True, verbose_name='Дата изменения')),
                ('is_draft', models.BooleanField(default=True, verbose_name='Опубликован')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='URl')),
            ],
            options={
                'verbose_name': 'Недвижимость',
                'verbose_name_plural': 'Недвижимость',
                'ordering': ('title',),
            },
        ),
    ]