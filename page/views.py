from django.shortcuts import redirect, render
from django.contrib import messages
from .models import (Carousel, Page)
from .forms import CarouselModelForm, PageModelForm
from django.utils.text import slugify

# kullanici icin
def index(request):
    context = dict()
    context['images'] = Carousel.objects.filter(
        status="published").exclude(cover_image='')
    # context['images'] = images
    return render(request, 'home/index.html', context)


def manage_list(request):
    context = {}
    return render(request, 'manage/manage.html', context)


def page_list(request):
    context = dict()
    context['items'] = Page.objects.all().order_by('-pk')
    return render(request, 'manage/page_list.html', context)


def page_create(request):
    context = dict()
    context['title'] = 'Paga create form'
    context['form'] = PageModelForm()
   
    if request.method == 'POST':
        form = PageModelForm(request.POST, request.FILES)
        if form.is_valid():
            slg = form.save(commit=False)
            slg.slug = slugify(slg.title)
            slg.save()
        messages.success(request, 'Page bir seyler eklendi  eklendi taslak')
    return render(request, 'manage/carousel_form.html', context)


# def carousel_update(request, pk):
#     form = CarouselModelForm()
#     context = {
#         'form': form
#     }
#     item = Carousel.objects.get(pk=pk)
#     context['form'] = CarouselModelForm(instance=item)

#     if request.method == 'POST':
#         form = CarouselModelForm(request.POST, request.FILES, instance=item)
#         print(form)
#         if form.is_valid():
#             form.save()
#         messages.success(request, 'Guncellendi Carousel guncellendi')
#         # return redirect('carousel_list')
#         return redirect('carousel_update', pk)
#     return render(request, 'manage/carousel_form.html', context)





# adminler icin
# stuff not checked


def carousel_list(request):
    form = CarouselModelForm()
    context = {
        'form': form
    }
    context['form'] = Carousel.objects.all().order_by('-pk')
    return render(request, 'manage/carousel_list.html', context)


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
    return render(request, 'manage/carousel_form.html', context)


def carousel_update(request, pk):
    form = CarouselModelForm()
    context = {
        'form': form
    }
    item = Carousel.objects.get(pk=pk)
    context['form'] = CarouselModelForm(instance=item)

    if request.method == 'POST':
        form = CarouselModelForm(request.POST, request.FILES, instance=item)
        print(form)
        if form.is_valid():
            form.save()
        messages.success(request, 'Guncellendi Carousel guncellendi')
        # return redirect('carousel_list')
        return redirect('carousel_update', pk)
    return render(request, 'manage/carousel_form.html', context)


# bu da alternativ yoll
""" def carousel_form(request=None, instance=None):
    if request:
        form = CarouselModelForm(
            request.POST,
            request.FILES,
            instance=instance
        )
    else:  
        form = CarouselModelForm(request, instance=instance)
    return form
 """
