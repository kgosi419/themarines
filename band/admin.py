from django.contrib import admin
from .models import Song

# Register your models here.

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Song instances.

    This class customizes the display and functionality of the Song model
    in the Django admin site. It specifies the fields that will be shown
    in the list view.

    Attributes:
        list_display (tuple): A tuple of field names that will be displayed
            in the admin list view for the Song model.
    """

    list_display = ('title', 'artist', 'album', 'release_date', 'genre')
