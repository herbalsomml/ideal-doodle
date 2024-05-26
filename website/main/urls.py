from django.urls import include, path

from . import views

app_name = 'main'

urlpatterns = [path('',
                    views.StudioListView.as_view(),
                    name='index'),
               path('search/',
                    views.StudioSearchList.as_view(),
                    name='studio_search'),
               path('studio/<slug:slug>/',
                    views.StudioDetailView.as_view(),
                    name='studio_detail'),]
