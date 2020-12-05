from django.contrib import admin
from .models import Category, Product

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'pk',
        'title',
        'slug',
        'gender',
        'status',
        'updated_at',
    )
    list_filter = ('status', 'gender' )
    list_editable = (
        'title',
        'status',
        'gender',
    )


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'pk',
        'title',
        'price',
        'stock',
        'slug',
        'status',
        'updated_at',
        'cover_image',
    )
    list_filter = ('status', )
    list_editable = (
        'title',
        'status',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
