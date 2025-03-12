from django.db import models

# Create your models here.


class Song(models.Model):
    """
    Represents a song in the music database.


    Args:
        models (Model): The base class from which the Song model inherits.


    Returns:
            None: This class does not return anything on instantiation.
    """
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)

    def __str__(self):
        """
        Returns a string representation of the song.


        Returns:
                str: A string representation of the song, combining the title and artist
        """
        return self.title
