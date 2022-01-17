from itertools import product
from django.core import paginator
from django.shortcuts import render,redirect
from .models import *
from .forms import OrderForm
#+from .forms import ProductForm
#from .models import Product

from django.core.paginator import Paginator
# Create your views here.
def greeting(request):
    data={}
    product_objects= Product.objects.all()
    item_name=request.GET.get("item_name")
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)
    data['productobj'] = product_objects

    paginator= Paginator (product_objects, 10)
    page=request.GET.get('page')
    product_objects = paginator . get_page(page)
    data['productobj'] = product_objects
    return render(request, "greeting.html", context=data)

def list_customer(request):
  data={}
  customers = Customer.objects.all()
  data['cus'] = customers
  return render(request, "list_customers.html", context=data)    

def detail_viwe(request,id):
    data={}
    product=Product.objects.get(id=id)
    data['product']=product
    return render(request,'detail.html',data)

def create_order(request):
  data = {}
  f = OrderForm(request.POST or None)
  data["form"] = f
  if f.is_valid():
    f.save()
    return redirect("greeting")
  return render (request, "create_order.html", context=data)    
    
def cart(request,cid):
    data={}
    #order_record=Order.objects.get(id=cid)
    #data['crt']=order_record
    return render(request,'store/cart.html',data)

def checkout(request):
    data={}
    return render(request,'store/checkout.html',data)    


#def search_poducts(request,id):
    #data={}
    #f=Product.objects.get(id=id)
    #data['search']=f
    #return render(request,'greeting.html',data)


def list_products(request):
  data={}
  product = Product.objects.all()
  data['prt'] = product
  return render(request, "products.html", data)   
    


