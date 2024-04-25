from django.urls import include, path

from . import views

app_name = 'main'

urlpatterns = [path('',
                    views.VideoListView.as_view(),
                    name='index'),
               path('videos-json/<int:num_videos>/',
                    views.VideoJsonListView.as_view(),
                    name='video-json-view')]
