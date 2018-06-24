from django.conf.urls import url
from . import views

app_name = 'music_ns'

urlpatterns = [
    url(r'^$',views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$' ,views.DetailView.as_view(),name='detail'),

    #/music/album/add/
    url(r'^album/add/$', views.CreateAlbum.as_view(),name='addAlbum'),

    #/music/album/pk-value/
    url(r'^(?P<pk>[0-9]+)/$' ,views.UpdateAlbum.as_view,name='updateAlbum'),

    #/music/album/pk-value/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$' ,views.DeleteAlbum.as_view,name='deleteAlbum'),
]