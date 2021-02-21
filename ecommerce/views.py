from django.shortcuts import render,get_object_or_404
from .models import CategoryOfProducts, Product

# Create your views here.
def list_of_product(request, category_slug=None):
    categories = CategoryOfProducts.objects.all()
    category = None
    products = Product.objects.filter(availability=True)
    if category_slug:
        category = get_object_or_404(CategoryOfProducts, slug=category_slug)
        products = products.filter(category=category)
    return render(request,'templates/list.html', {'category': category, 'categories': categories, 'products': products})

def single_product(request, id, slug):
    product = get_object_or_404(Product, id=id,slug=slug,availability=True)
    return render(request,'templates/product.html',{'product': product})