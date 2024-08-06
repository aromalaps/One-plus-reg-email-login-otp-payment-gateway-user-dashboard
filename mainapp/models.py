from django.db import models
from django.urls import reverse
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    items=models.CharField(max_length=250,unique=True)

    class Meta:
        ordering=('name',)

    def __str__(self):
        return self.name
    def get_url(self):
        return reverse('Products:product_by_category',args=[self.slug])
   
class Product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    detail=models.CharField(max_length=500)
    image=models.ImageField(upload_to='category',blank=True)
    price=models.IntegerField()
    color=models.CharField(max_length=250)
    storage=models.CharField(max_length=250)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('name',)

    def __str__(self):
        return self.name
class NewProduct(models.Model):
    ids=models.IntegerField()
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField(blank=True)
    Banner=models.ImageField(upload_to='category',blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('id',)

    def __str__(self):
        return self.name
        