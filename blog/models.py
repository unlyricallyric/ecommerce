from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.TextField()
    slug = models.SlugField(unique = True) # hello world -> hello-world
    content = models.TextField(null=True, blank=True)

