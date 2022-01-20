from itertools import product
from pyexpat import model
from django.core import paginator
from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from .forms import OrderForm
#+from .forms import ProductForm
#from .models import Product

from django.core.paginator import Paginator
# Create your views here.
def greeting(request):
    data={}
    product_objects= Product.objects.all()
    #item_name=request.GET.get("item_name")
    #if item_name != '' and item_name is not None:
        #product_objects = product_objects.filter(title__icontains=item_name)
    data['productobj'] = product_objects

    #paginator= Paginator (product_objects, 10)
    #page=request.GET.get('page')
    #product_objects = paginator . get_page(page)
    #data['productobj'] = product_objects
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
    
def cart(request):
    data={}
    customer =Customer.objects.filter(name="Ranya Ayman")
    order, created = Order.objects.get_or_create(customer=customer)
    items= order.orderitem_set.all()
    data= {'items': items}
    return render(request,'store/cart.html',data)

def checkout(request):
    data={}
    return render(request,'store/checkout.html',data)    


def search_poducts(request):
  data = {}
  search = request.POST["search"]
  searched_p = Product.objects.filter(title__contains=search)
  data['search'] = search
  data['searched_p']=searched_p
  return render(request, "search_p.html", context=data)
    
    

def list_products(request):
  data={}
  product = Product.objects.all()
  data['prt'] = product
  return render(request, "products.html", data)   
    


