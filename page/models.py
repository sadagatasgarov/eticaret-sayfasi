from django.db import models
from django.utils.text import slugify

# Create your models here.
DEFAULT_STATUS = 'draft'
STATUS = [
    ('draft', 'Taslak'),
    ('published', 'Yayinlandi'),
    ('deleted', 'Silindi'),
]


class Page(models.Model):
    # title
    title = models.CharField(max_length=200)

    # slug
    slug = models.SlugField(max_length=200, default="")

    # content
    content = models.TextField()

    # cover_image
    cover_image = models.ImageField(
        upload_to='page',
        null=True,
        blank=True,
    )
    # status
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10
    )

    # created_at
    created_at = models.DateTimeField(auto_now_add=True)

    # updated_at
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.title


class Carousel(models.Model):
    # title
    title = models.CharField(max_length=200, blank=True, null=True)
    # cover_image
    cover_image = models.ImageField(
        upload_to='carousel',
        null=True,
        blank=True,
    )

    # status
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10
    )

    # created_at
    created_at = models.DateTimeField(auto_now_add=True)

    # updated_at
    updated_at = models.DateTimeField(auto_now=True)
