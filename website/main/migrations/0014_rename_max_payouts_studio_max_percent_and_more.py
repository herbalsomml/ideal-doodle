# Generated by Django 4.2.13 on 2024-05-25 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_experiencechoices_formatchoices_genderchoices_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studio',
            old_name='max_payouts',
            new_name='max_percent',
        ),
        migrations.RenameField(
            model_name='studio',
            old_name='min_payouts',
            new_name='min_percent',
        ),
    ]
