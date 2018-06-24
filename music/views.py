from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from  django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404
from .models import Album
from django.views import View

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    # context_object_name = 'object_list' #this is the default name
    context_object_name = 'albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'
    context_object_name = 'albums'

class CreateAlbum(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class UpdateAlbum(UpdateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class DeleteAlbum(DeleteView):
    model = Album
    success_url = reverse_lazy('music_ns:index')




