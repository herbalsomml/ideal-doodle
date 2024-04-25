# Generated by Django 5.0.4 on 2024-04-25 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_video_options_video_to_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100, verbose_name='Вопрос')),
                ('answer', models.TextField(verbose_name='Ответ')),
                ('is_published', models.BooleanField(default=True, help_text='Снимите галочку, чтобы скрыть публикацию.', verbose_name='Опубликовано')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')),
                ('pub_date', models.DateTimeField(help_text='Если установить дату и время в будущем — можно делать отложенные публикации.', verbose_name='Дата и время публикации')),
            ],
            options={
                'verbose_name': 'вопрос',
                'verbose_name_plural': 'Вопросы',
                'ordering': ('-pub_date',),
                'default_related_name': 'questions',
            },
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'default_related_name': 'videos', 'ordering': ('-pub_date',), 'verbose_name': 'видео', 'verbose_name_plural': 'Видео'},
        ),
        migrations.AlterField(
            model_name='video',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Добавлено'),
        ),
        migrations.AlterField(
            model_name='video',
            name='to_slider',
            field=models.BooleanField(default=False, verbose_name='Добавить в слайдер'),
        ),
    ]
