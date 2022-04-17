from pyexpat import model
from django.db import models
from django.utils.text import slugify

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default='', db_index=True)
    image = models.ImageField(upload_to='post_images/', blank=True)
    tags = models.ManyToManyField(Tag, related_name='posts')
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name='posts')

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=100)
    text = models.TextField()
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
