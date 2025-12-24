from django.db import models
from django.utils.text import slugify 
import re
import unicodedata
class USER(models.Model):
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    email = models.EmailField()
    slug = models.SlugField(
    max_length=191,
    unique=True,
    db_index=True
)

    def generate_slug(self):
        return f"{self.user_name}-{self.email}".lower()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.generate_slug())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user_name


class Task_Create(models.Model):
    title = models.CharField(max_length=50, null=True)
    description = models.TextField()
    status = models.CharField(max_length=20)
    create_date = models.DateTimeField(auto_now_add=True)
    User = models.ForeignKey(USER, on_delete=models.CASCADE)
    slug = models.SlugField(
    max_length=191,
    unique=True,
    db_index=True
)

    def generate_slug(self):
        return f"{self.title}-{self.status}".lower()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.generate_slug())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
