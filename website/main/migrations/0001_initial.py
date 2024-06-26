# Generated by Django 5.0.4 on 2024-04-25 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90, verbose_name='Название видео')),
                ('short_description', models.CharField(max_length=50, verbose_name='Короткое описание')),
                ('description', models.TextField(verbose_name='Полное описание')),
                ('slug', models.SlugField(help_text='Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.', unique=True, verbose_name='Идентификатор')),
                ('image', models.ImageField(upload_to='post_images', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'видео',
                'verbose_name_plural': 'Видео',
                'ordering': ('-id',),
                'default_related_name': 'videos',
            },
        ),
    ]
