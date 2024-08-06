from django.contrib import admin
from .models import Category,Product,NewProduct
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug','items']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','stock','available','created','updated']
    prepopulated_fields={'slug':('name',)}
    list_editable=['price','stock','available']
    list_per_page=20
admin.site.register(Product,ProductAdmin) 

class NewProductAdmin(admin.ModelAdmin):
    list_display=['ids','name','price','Banner','created','updated']
    prepopulated_fields={'slug':('name',)}
    list_editable=['price','Banner']
    list_per_page=20

admin.site.register(NewProduct,NewProductAdmin) 