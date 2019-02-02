from django.db import models
from django.template.defaultfilters import slugify
import unidecode
from unidecode import unidecode
# Create your models here.


class Post(models.Model):
    city = models.CharField(max_length=50, db_index=True)
    title = models.CharField(max_length=200, db_index=True)
    address = models.CharField(max_length=150, db_index=True)
    time = models.CharField(max_length=100, db_index=True)
    price = models.CharField(max_length=50, db_index=True)
    info = models.TextField(blank=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.title)