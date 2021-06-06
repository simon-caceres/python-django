""" Users Models. """

from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import files

class Profile(models.Model):
    """ Profile model.
        Proxy model that extends the base data with other information
    """
    #Cascade imita el Cascade de sql logic
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE
    )
    

    website = models.URLField(max_length=200, blank=True)

    biography = models.TextField(blank=True)

    phone_number = models.CharField(max_length=12, blank=True)

    picture = models.ImageField(
        upload_to = 'users/pictures', 
        blank=True, 
        null = True
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return super().__str__()
