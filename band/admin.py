from django.contrib import admin
from .models import Song

# Register your models here.

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing Song instances in the Django admin interface.


    Args:
        models (ModelAdmin): Inherited class from Django's ModelAdmin for configuring various
                             admin options related to the Song model.

    """
    list_display = ('title', 'artist', 'album', 'release_date', 'genre')
