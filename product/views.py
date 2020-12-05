from django.shortcuts import render, get_object_or_404
from product.models import Product, Category

# Create your views here.
def category_show(request, category_slug):
    context = dict()
    context['category'] = get_object_or_404(Category, slug = category_slug)
    
    #Nav icin
    # context['categories'] = Category.objects.filter(
    #     status = 'published'
    # )
    
    context['items'] = Product.objects.filter(
        category = context['category'],
        status = 'published',
        stock__gte = 1,
    )
   
    return render(request, 'product/category_show.html', context)