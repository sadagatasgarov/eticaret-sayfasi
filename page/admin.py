from django.contrib import admin
from .models import Page, Carousel

# Register your models here.


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = [
        'pk',
        'title',
        'created_at',
        'updated_at',
        'slug',
    ]

    list_filter = [
        'status'
    ]

    search_fields = ['title']

    list_display_links = ['title']


admin.site.register(Page, PageAdmin)
admin.site.register(Carousel)




# @admin.register(Page)
# class PageAdmin(admin.ModelAdmin):
#     list_display = ['title', 'created_at']
#     list_display_link = ['title']
#     class Meta:
#         model = Page

# @admin.register(Carousel)
# class CarouselAdmin(admin.ModelAdmin):
#     class Meta:
#         model = Carousel