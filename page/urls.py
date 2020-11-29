from django.urls import path
from .views import (
    # Manage
    manage_list,


    # Page
    page_list,
    page_create,


    # Carousel
    carousel_create,
    carousel_update,
    carousel_list,
)


urlpatterns = [
    # Manage
    path('', manage_list, name='manage_list'),
    


    # Page
    path('page/list', page_list, name='page_list'),
    path('page/create', page_create, name='page_create'),

    # Carousel
    path('carousel_list/', carousel_list, name='carousel_list'),
    path('carousel_create/', carousel_create, name='carousel_create'),
    path('carousel_update/<int:pk>/', carousel_update, name='carousel_update'),


]
