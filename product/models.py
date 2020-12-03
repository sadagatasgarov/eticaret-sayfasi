from django.db import models
from page.models import STATUS, DEFAULT_STATUS
# Create your models here.
# Category

GENDER_CHOICE = [
    ("men","Erkek"),
    ("women","Kadin"),
    ("unisex","UniSex"),
]

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=200,
        default="",
    )

    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10,
    )

    gender = models.CharField(
        max_length=6,
        default = 'unisex',
        choices = GENDER_CHOICE
        )
    createt_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pk +1000}-{self.gender} - {self.title}"


# Product
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=200,
        default="",
    )
    content = models.TextField()

    cover_image = models.ImageField(
        upload_to='page',
        null=True,
        blank=True,
    )
    stock = models.PositiveSmallIntegerField()

    price = models.FloatField()

    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10,
    )
    createt_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
