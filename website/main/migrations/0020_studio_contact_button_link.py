# Generated by Django 4.2.13 on 2024-05-25 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_studio_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='studio',
            name='contact_button_link',
            field=models.CharField(default='#', max_length=128, verbose_name='Ссылка для кнопки связаться премиума'),
        ),
    ]
