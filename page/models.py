from django.db import models

# Create your models here.
STATUS = [
    ('draft','Taslak'),
    ('published','Yayinlandi'),
    ('deleted','Silindi'),
]


class Page(models.Model):
    #title
    title = models.CharField(max_length=200)

    #content
    content = models.TextField()

    #slug

    #cover_image
    cover_image = models.ImageField(upload_to='page')

    #status
    status = models.CharField(
        default='draft',
        choices=STATUS,
        max_length=10
    )

    #created_at
    created_at = models.DateTimeField(auto_now_add=True)

    #updated_at
    updated_at = models.DateTimeField(auto_now=True)