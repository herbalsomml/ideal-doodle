from django.db import models
from django.utils import timezone


class Question(models.Model):
    question = models.CharField(
        max_length=100,
        blank=False,
        verbose_name='Вопрос'
    )
    answer = models.TextField(
        blank=False,
        verbose_name='Ответ'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено'
    )
    position = models.IntegerField()

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ('position',)
        default_related_name = 'questions'

    def __str__(self):
        if len(self.question) > 25:
            return self.question[:25] + '...'
        return self.question


class Video(models.Model):
    title = models.CharField(
        max_length=90,
        blank=False,
        verbose_name='Название видео'
    )
    short_description = models.CharField(
        max_length=50,
        blank=False,
        verbose_name='Короткое описание',
    )
    description = models.TextField(
        verbose_name='Полное описание'
    )
    link = models.URLField(
        blank=False
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text=('Если установить дату и время в будущем'
                   ' — можно делать отложенные публикации.')
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text=('Идентификатор страницы для URL;'
                   ' разрешены символы латиницы,'
                   ' цифры, дефис и подчёркивание.')
    )
    image = models.ImageField('Фото', upload_to='video_images', blank=False)
    to_slider = models.BooleanField(
        default=False,
        verbose_name='Добавить в слайдер'
    )

    class Meta:
        verbose_name = 'видео'
        verbose_name_plural = 'Видео'
        ordering = ('-pub_date',)
        default_related_name = 'videos'

    def __str__(self):
        if len(self.title) > 25:
            return self.title[:25] + '...'
        return self.title

    @staticmethod
    def get_published_videos():
        current_time = timezone.now()
        video_list = Video.objects.filter(
            is_published=True,
            pub_date__lte=current_time
        )
        video_slider_list = video_list.filter(to_slider=True)
        return video_list, video_slider_list
