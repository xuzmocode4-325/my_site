from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

# Create your models here.
class Author(models.Model):
    avatar = models.ImageField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username =  models.CharField(max_length=100, unique=True)
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

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=255)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True
    )
    content = models.TextField(validators=[MinLengthValidator(255)])
    author = models.ForeignKey(
        Author, related_name='posts', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Project(models.Model): 
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    image = models.ImageField(max_length=250)
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


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User, related_name='comments', on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return f"{self.user} on {self.post}"

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