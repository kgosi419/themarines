from django.db import models

# Create your models here.


class Song(models.Model):
    """
    A representation of a music song.

    Attributes:
        title (str): The title of the song.
        artist (str): The name of the artist who performed the song.
        album (str): The name of the album containing the song.
        release_date (date): The release date of the song.
        genre (str): The genre of the song.
    """

    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)

    def __str__(self):
        """
        Return a string representation of the Song instance.

        Returns:
            str: The title of the song.
        """
        return self.title
