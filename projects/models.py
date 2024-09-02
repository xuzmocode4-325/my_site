from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from my_site.models import Author, Tag

class Project(models.Model): 
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to="images/projects")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True
    )
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

# Create your models here.
class Review(models.Model):
    project = models.ForeignKey(
        Project, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='reviews', on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return f"{self.user} on {self.project}"