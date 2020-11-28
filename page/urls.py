from django.urls import path
from .views import (
    #Manage




    #Carousel
    carousel_create,
    carousel_update,
    carousel_list,
  )


urlpatterns = [
    #Manage
    path('carousel_list/', carousel_list, name='carousel_list'),
    
    
    
    
    #Carousel
    path('carousel_list/', carousel_list, name='carousel_list'),
    path('carousel_create/', carousel_create, name='carousel_create'),
    path('carousel_update/<int:pk>/', carousel_update, name='carousel_update'),
  

]
