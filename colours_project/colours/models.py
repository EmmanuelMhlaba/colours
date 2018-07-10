from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

class Palette(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    #def get_absolute_url(self):
    #    return reverse('colours:details', args=[str(self.slug)])

    def __str__(self):
        return self.name


class Colour(models.Model):
    palette = models.ForeignKey(Palette, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, unique=True)
    hex_code = models.CharField(max_length=7, unique=True)
    additional_info = models.TextField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    #def get_absolute_url(self):
    #    return reverse('colours:details', args=[str(self.slug)])

    def __str__(self):
        return self.name

