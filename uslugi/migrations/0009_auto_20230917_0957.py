# Generated by Django 3.2.19 on 2023-09-17 06:57

from django.db import migrations, models
import django.db.models.deletion
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('uslugi', '0008_auto_20230917_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoprosOtvet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vopros', models.TextField(blank=True, max_length=3000, verbose_name='Вопрос')),
                ('otvet', django_ckeditor_5.fields.CKEditor5Field(blank=True, max_length=10000, verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'Вопрос - Ответ',
                'verbose_name_plural': 'Вопрос - Ответ',
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='uslugi',
            name='vopotv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='uslugi.voprosotvet', verbose_name='Вопрос- Ответ'),
        ),
    ]
