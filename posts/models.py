from django.db import models

class User(models.Model):
    #User Model.
    email = models.EmailField(unique=True)
    password = models.CharField(max_length= 30)
    first_name = models.CharField(max_length= 30)
    last_name = models.CharField(max_length= 30)
    bio = models.TextField(blank=True)

    fs_admin =  models.BooleanField(default=False)

    birthdate = models.DateField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return super().__str__()