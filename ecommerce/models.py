from django.db import models

# Create your models here.

class CategoryOfProducts(models.Model):
    """Model for categories of products"""
    category_name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200,unique = True)

    class Meta:
        ordering = ('category_name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name

class Product(models.Model):
    """Model for products"""
    product_name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200,db_index=True)
    category = models.ForeignKey(CategoryOfProducts,related_name='products',on_delete= models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    description = models.TextField(blank=True)
    availability = models.BooleanField(default = True)
    price = models.DecimalField(max_digits=10, decimal_places = 2)
    creation_date = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ('product_name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.product_name

 
