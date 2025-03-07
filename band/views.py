from django.shortcuts import render
from .models import Song
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    """
    Render the home page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered home page.
    """
    return render(request, 'band/home.html')


def about(request):
    """
    Render the about page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered about page.
    """
    return render(request, 'band/about.html')


@login_required
def music(request):
    """
    Render the music page, showing a list of all songs.

    This view requires user authentication. Only logged-in users can access this page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered music page with the list of songs.
    """
    songs = Song.objects.all()
    return render(request, 'band/music.html', {'songs': songs})


def music_page(request):
    """
    Render a specific music page, showing a list of all songs.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered music page with the list of songs.
    """
    songs = Song.objects.all()  # Fetch all song entries
    return render(request, 'music/music_page.html', {'songs': songs})
