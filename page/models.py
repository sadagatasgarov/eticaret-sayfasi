from django.db import models
from django.utils.text import slugify

# Create your models here.
STATUS = [
    ('draft', 'Taslak'),
    ('published', 'Yayinlandi'),
    ('deleted', 'Silindi'),
]


class Page(models.Model):
    # title
    title = models.CharField(max_length=200)

    # slug
    #slug_text = slugify(title.replace("ı","i").replace("ə","e").replace("ş","sh"))
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
        default='draft',
        choices=STATUS,
        max_length=10
    )

    # created_at
    created_at = models.DateTimeField(auto_now_add=True)

    # updated_at
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
