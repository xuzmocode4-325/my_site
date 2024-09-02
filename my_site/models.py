from django.db import models

class Author(models.Model):
    avatar = models.ImageField(upload_to="images/authors")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    bio = models.CharField(max_length=255)
    git_hub = models.CharField(max_length=50, unique=True)
    linked_in = models.CharField(max_length=100, unique=True)
    twitter = models.CharField(max_length=100, unique=True)
    email = models.EmailField()

    def robust_name(self):
        return f'{self.first_name} {self.username} {self.last_name}'

    def __str__(self):
        return self.username


class Tag(models.Model):
    caption = models.CharField(max_length=25)

    def __str__(self):
        return self.caption