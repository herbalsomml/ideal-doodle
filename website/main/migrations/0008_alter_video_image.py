# Generated by Django 5.0.4 on 2024-04-25 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_video_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='image',
            field=models.ImageField(upload_to='video_imagess', verbose_name='Фото'),
        ),
    ]
