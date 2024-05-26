# Generated by Django 4.2.13 on 2024-05-25 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_studio_max_payouts_studio_min_payouts_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studio',
            name='cities',
        ),
        migrations.AddField(
            model_name='studio',
            name='cities',
            field=models.ManyToManyField(to='main.city', verbose_name='Города работы'),
        ),
    ]
