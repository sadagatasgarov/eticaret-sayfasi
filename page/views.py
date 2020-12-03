from django.shortcuts import redirect, render
from django.contrib import messages
from .models import (Carousel, Page)
from .forms import CarouselModelForm, PageModelForm
from django.utils.text import slugify
from django.contrib.admin.views.decorators import staff_member_required

from product.models import Category

# kullanici icin


def index(request):
    context = dict()
    context['images'] = Carousel.objects.filter(
        status="published").exclude(cover_image='')
    # context['images'] = images

    context['categories'] = Category.objects.filter(
        status='published'
    )
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
    context['title'] = 'Page create form'
    context['form'] = PageModelForm()

    if request.method == 'POST':
        form = PageModelForm(request.POST, request.FILES)
        if form.is_valid():
            slg = form.save(commit=False)
            slg.slug = slugify(slg.title.replace('ı', 'i'))
            slg.save()

        messages.success(request, 'Page bir seyler eklendi  eklendi taslak')
        return redirect('page_list')
    return render(request, 'manage/form.html', context)


@staff_member_required
def page_update(request, pk):
    form = PageModelForm()
    context = {
        'form': form
    }

    item = Page.objects.get(pk=pk)
    context['title'] = f'{item.title} -id: {item.pk} Carousel create form'
    context['form'] = PageModelForm(instance=item)

    if request.method == 'POST':
        form = PageModelForm(request.POST, request.FILES, instance=item)
        print(form)
        if form.is_valid():
            slg = form.save(commit=False)
            if item.slug == '':
                slg.slug = slugify(slg.title.replace('ı', 'i'))
            slg.save()
        messages.success(request, 'Guncellendi Carousel guncellendi')
        # return redirect('carousel_list')
        return redirect('page_update', pk)
    return render(request, 'manage/form.html', context)


def page_delete(request, pk):
    item = Page.objects.get(pk=pk)
    item.status = "deleted"
    item.save()

    return redirect('page_list')


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
    context['title'] = 'Carousel create form'
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
    return render(request, 'manage/form.html', context)


def carousel_update(request, pk):
    form = CarouselModelForm()
    context = {
        'form': form
    }

    item = Carousel.objects.get(pk=pk)
    context['title'] = f'{item.title} -id: {item.pk} Carousel create form'
    context['form'] = CarouselModelForm(instance=item)

    if request.method == 'POST':
        form = CarouselModelForm(request.POST, request.FILES, instance=item)
        print(form)
        if form.is_valid():
            form.save()
        messages.success(request, 'Guncellendi Carousel guncellendi')
        # return redirect('carousel_list')
        return redirect('carousel_update', pk)
    return render(request, 'manage/form.html', context)


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
