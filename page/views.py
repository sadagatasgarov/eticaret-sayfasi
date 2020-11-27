from django.shortcuts import render
from django.contrib import messages
from .models import Carousel
from .forms import CarouselModelForm

# kullaici icin
def index(request):
    context = dict()
    context['images'] = Carousel.objects.filter(status="published").exclude(cover_image = '')
    # context['images'] = images
    return render(request, 'home/index.html', context)




#adminler icin
# stuff not checked
def carousel_create(request):
    context = dict()
    context['form'] = CarouselModelForm()
    # item = Carousel.objects.first()
    # context['form'] = CarouselModelForm(instance=item)

    if request.method == 'POST':
        print(request.POST)
        print(request.FILES.get('cover_image'))
        # create code is deleted
        form = CarouselModelForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
        messages.success(request, 'Carousele resim  eklendi taslak')
    return render(request, 'manage/carousel_create.html', context)


def carousel_list(request):
    form = CarouselModelForm()
    context = {
        'form' : form
    }
    context['form'] = Carousel.objects.all()
    return render(request, 'manage/carousel_list.html', context)
    


def carousel_update(request, pk):
    form= CarouselModelForm()
    context = {
        'form':form
    }
    item = Carousel.objects.first()
    context['form'] = CarouselModelForm(instance=item)

    if request.method == 'POST':
        print(request.POST)
        print(request.FILES.get('cover_image'))
        # create code is deleted
        form = CarouselModelForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
        messages.success(request, 'Guncellendi Carousel guncellendi')
    return render(request, 'manage/carousel_create.html', context)