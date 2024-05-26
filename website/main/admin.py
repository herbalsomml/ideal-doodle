from django.contrib import admin

from .models import Question, Video

admin.site.register(Video)
admin.site.register(Question)
