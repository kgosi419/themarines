from django.shortcuts import render
from .models import Song
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'band/home.html')


def about(request):
    return render(request, 'band/about.html')


@login_required
def music(request):
    songs = Song.objects.all()
    return render(request, 'band/music.html', {'songs': songs})


def music_page(request):
    songs = Song.objects.all()  # Fetch all song entries
    return render(request, 'music/music_page.html', {'songs': songs})
