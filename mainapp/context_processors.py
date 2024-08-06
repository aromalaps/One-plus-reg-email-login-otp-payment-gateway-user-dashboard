from .models import Category,Product,NewProduct

def menu_links(req):
    links=Category.objects.all()
    return dict(links=links)
def products(req):
    phone=Product.objects.all()
    return dict(phone=phone)
def newproduct(req):
    newphone=NewProduct.objects.all()
    return dict(newphone=newphone) 