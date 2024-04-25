from django.db import models


class SiteSettings(models.Model):
    model_name = models.CharField(
        max_length=256,
        verbose_name='Имя модели',
        blank=False,
        default='Herbal Sommelier'
    )
    site_title = models.CharField(
        max_length=128,
        verbose_name='Название страницы',
        blank=False,
        default='Herbal Sommelier - Content creator 18+'
    )
    site_url = models.URLField(
        max_length=256,
        verbose_name='Ссылка на сайт',
        blank=False,
        default='https://www.herbalsomml.online/'
    )
    videos_button_nav_text = models.CharField(
        max_length=30,
        verbose_name='Текст кнопки блока видео в меню',
        blank=False,
        default='Videos'
    )
    links_button_nav_text = models.CharField(
        max_length=15,
        verbose_name='Текст кнопки блока ссылок в меню',
        blank=False,
        default='Links'
    )
    qa_button_nav_text = models.CharField(
        max_length=15,
        verbose_name='Текст кнопки блока вопросов в меню',
        blank=False,
        default='Q&A'
    )
    subscribe_button_text_one = models.CharField(
        max_length=15,
        verbose_name='Первая часть текста кнопки подписки',
        blank=False,
        default='Subscribe'
    )
    subscribe_button_text_two = models.CharField(
        max_length=15,
        verbose_name='Вторая часть текста кнопки подписки',
        blank=False,
        default='and watch'
    )
    watch_button_text = models.CharField(
        max_length=30,
        verbose_name='Текст кнопки просмотра',
        blank=False,
        default='Watch it!'
    )
    fansly_url = models.URLField(
        max_length=256,
        verbose_name='Ссылка на Fansly',
        blank=False,
        default='https://www.fans.ly/r/herbalsomml/'
    )
    instagram_url = models.URLField(
        max_length=256,
        blank=False,
        verbose_name='Ссылка на Instagram',
        default='https://www.instagram.com/herbalsomml/'
    )
    twitter_url = models.URLField(
        max_length=256,
        blank=False,
        default='https://www.twitter.com/herbalsomml/',
        verbose_name='Ссылка на Twitter'
    )
    telegram_url = models.URLField(
        max_length=256,
        blank=False,
        default='https://t.me/+SNEN4dqJJR9jY2Yy/',
        verbose_name='Ссылка на Telegram'
    )
    chaturbate_url = models.URLField(
        max_length=256,
        verbose_name='Ссылка на Chaturbate',
        blank=False,
        default=('https://chaturbate.com/in/?tour=dT8X&campaign'''
                 '''=rvN8K&track=default&room=herbal_sommelier''')
    )
    stripchat_url = models.URLField(
        max_length=256,
        blank=False,
        default='https://stripchat.com/AyeBassota/follow-me',
        verbose_name='Ссылка на Stripchat'
    )
    videos_block_header = models.TextField(
        blank=False,
        default='Newest videos!',
        verbose_name='Заголовок блока видео'
    )
    load_more_button_text = models.CharField(
        max_length=30,
        verbose_name='Текст кнопки загрузки контента',
        blank=False,
        default='Load more'
    )
    running_line_text = models.CharField(
        verbose_name='Текст бегущей строки',
        blank=False,
        default=('FIRST MONTH -20% • A LOT OF HOT CONTENT '''
                 '''• $0,32 PER A DAY • SUBSCRIBE AND WATCH!'''),
        max_length=1024
    )
    fansly_block_header = models.TextField(
        blank=False,
        default='Subscribe to my Fansly!',
        verbose_name='Заголовок блока Fansly'
    )
    fansly_block_image = models.ImageField(
        blank=False,
        upload_to='video_images',
        verbose_name='Фото для блока Fansly'
    )
    fansly_block_text = models.TextField(
        blank=False,
        default=('<h3>🔥 A lot of hot videos and photos</h3><h3>📷 '''
                 '''New photo every day</h3><h3>'''
                 '''📹 New long video every few days</h3><h3>💬 ''
                 ''''Private messages and chat with '''
                 '''me</h3><h3>🎫 Free entry to ticket shows'''
                 ''' on Chaturbate</h3>'''
                 '''<h3>🎁 Special gift</h3><br>'''),
        verbose_name='Текст блока Fansly'
    )
    fansly_button_text = models.CharField(
        max_length=40,
        blank=False,
        default='Subscribe and get 1 day free',
        verbose_name='Текст кнопки в блоке Fansly'
    )
    webcam_block_header = models.TextField(
        blank=False,
        default='Join my live shows!',
        verbose_name='Заголовок блока Webcam'
    )
    webcam_block_image = models.ImageField(
        blank=False,
        upload_to='video_images',
        verbose_name='Фото для блока Webcam'
    )
    webcam_block_text = models.TextField(
        blank=False,
        default=('<h3>We can chat together, do naughty things,'''
                 ''' or just have a great time together 😊</h3><br>'''),
        verbose_name='Текст блока Webcam'
    )
    social_media_block_header = models.TextField(
        verbose_name='Заголовок блока социальных сетей',
        blank=False,
        default='Follow my social pages!'
    )
    social_media_block_image = models.ImageField(
        blank=False,
        upload_to='video_images',
        verbose_name='Фото для блока социальных сетей'
    )
    social_media_block_text = models.TextField(
        verbose_name='Текст блока социальных сетей',
        blank=False,
        default=(
            '''<h3>Enjoy free videos, photos and new announcements '''
            '''every day.</h3><h3>It\'s really hot!</h3><br>''')
    )
    qa_block_header = models.TextField(
        verbose_name='Заголовок блока вопрос ответ',
        blank=False,
        default='Questions & Answers'
    )

    def __str__(self):
        return self.site_url
