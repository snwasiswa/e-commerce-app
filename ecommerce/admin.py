from django.contrib import admin
from .models import CategoryOfProducts, Product

# Register your models here.

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    """Add the model to the Administration"""
    
    list_display = ['product_name', 'slug','availability', 'price','creation_date','update']
    list_filter = ['availability','creation_date','update']
    list_editable = ['availability','price']
    prepopulated_fields = {'slug':('product_name',)}


@admin.register(CategoryOfProducts)
class AdminCategory(admin.ModelAdmin):
    """Add the model to the Administration"""

    list_display = ['category_name','slug']
    prepopulated_fields = {'slug':('category_name',)}

