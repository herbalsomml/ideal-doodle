# Generated by Django 4.2.13 on 2024-05-25 07:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_video_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90, verbose_name='Название cтудии')),
                ('image', models.ImageField(upload_to='')),
                ('short_description', models.CharField(max_length=50, verbose_name='Короткое описание')),
                ('description', models.TextField(verbose_name='Полное описание')),
                ('telegram', models.CharField(max_length=128, verbose_name='Телеграм аккаунт')),
                ('website', models.URLField(max_length=258, verbose_name='Ссылка на сайт')),
                ('phone', models.CharField(max_length=40, verbose_name='Номер телефона')),
                ('experience', models.CharField(choices=[('noexperience', 'Без опыта'), ('less6month', 'Меньше 6 месяцев'), ('from6monthto1year', 'От 6 месяцев'), ('morethenyear', 'От года')], max_length=20)),
                ('format', models.CharField(choices=[('offline', 'Офлайн'), ('online', 'Онлайн')], max_length=20)),
                ('gender', models.CharField(choices=[('female', 'Девушки'), ('male', 'Парни'), ('couples', 'Пары'), ('trans', 'Транс')], max_length=20)),
                ('english', models.BooleanField(default=False)),
                ('min_age', models.IntegerField(default=18, verbose_name='Минимальный возраст модели')),
                ('max_age', models.IntegerField(default=60, verbose_name='Максильмальный возраст модели')),
                ('payouts', models.CharField(choices=[('everyday', 'Ежедневно'), ('1perweek', '1 раз в неделю'), ('1permonth', '1 раз в месяц'), ('2permonth', '2 раза в месяц')], max_length=30)),
                ('shifts', models.CharField(choices=[('morning', 'Утренние'), ('day', 'Дневные'), ('evening', 'Вечерние'), ('night', 'Ночные')], max_length=30)),
                ('operator', models.BooleanField(default=False, verbose_name='Наличие оператора')),
                ('cities', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.city')),
            ],
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
