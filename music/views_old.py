# from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Album, Song

# Create your views here.

def index(request):
    all_albums = Album.objects.all()
    return render(request,'music/index.html',{'album_names' : all_albums})

def detail(request, album_id):
    # try:
    #     all_albums=Album.objects.get(pk=album_id)
    # except Album.DoesNotExist:
    #     raise Http404("Album not forund")

    all_albums = get_object_or_404(Album, pk=album_id)
    return render(request,'music/detail.html',{'albums':all_albums})

def fav(request, album_id):
    all_albums = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = all_albums.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html',{
            'albums':all_albums,
            'error_message':'Please select a Song and revisit this page'
        })
    else:
        selected_song.is_fav = True
        selected_song.save()
        return render(request,'music/detail.html',{'albums' : all_albums})