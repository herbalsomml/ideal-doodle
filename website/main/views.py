from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView, View

from settings.models import SiteSettings

from .models import Question, Video


class VideoListView(ListView):
    model = Video
    template_name = 'main/index.html'
    context_object_name = 'video_list'

    def get_queryset(self):
        return Video.objects.filter(
            is_published=True,
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        video_slider_list = self.get_queryset().filter(to_slider=True)
        questions_list = Question.objects.filter(
            is_published=True
        ).order_by('position')
        settings_list = SiteSettings.objects.first()
        context['settings_list'] = settings_list
        context['questions_list'] = questions_list
        if video_slider_list.exists():
            context['video_slider_list'] = video_slider_list
        return context


class VideoJsonListView(View):
    def get(self, *args, **kwargs):
        print(kwargs)
        upper = kwargs.get('num_videos')
        lower = upper - 6
        videos = Video.objects.filter(
            is_published=True,
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')
        videos = list(videos.values())[lower:upper]
        videos_size = len(Video.objects.all())
        size = True if upper >= videos_size else False
        return JsonResponse({'data': videos, 'max': size}, safe=False)
