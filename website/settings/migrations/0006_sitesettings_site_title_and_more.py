# Generated by Django 5.0.4 on 2024-04-25 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_alter_sitesettings_fansly_block_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='site_title',
            field=models.CharField(default='Herbal Sommelier - Content creator 18+', max_length=128, verbose_name='Название страницы'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='model_name',
            field=models.CharField(default='Herbal Sommelier', max_length=256, verbose_name='Имя модели'),
        ),
    ]
