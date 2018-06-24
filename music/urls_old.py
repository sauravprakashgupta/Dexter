from django.conf.urls import url
from . import views

app_name = 'music_ns'

urlpatterns = [
    #/music/
    url(r'^$', views.index, name='index'),

    #/music/456/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    #/music/456/fav
    url(r'^(?P<album_id>[0-9]+)/fav/$', views.fav, name='fav'),
]
