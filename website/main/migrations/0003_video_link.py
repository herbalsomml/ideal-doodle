# Generated by Django 5.0.4 on 2024-04-25 08:38

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_video_options_video_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='link',
            field=models.URLField(default=datetime.datetime(2024, 4, 25, 10, 38, 45, 187528)),
            preserve_default=False,
        ),
    ]
