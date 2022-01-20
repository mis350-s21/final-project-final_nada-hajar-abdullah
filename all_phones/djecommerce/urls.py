"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.views.generic.base import TemplateView
urlpatterns = [
    path('', views.greeting, name='greeting'),
    path('list_customers/', views.list_customer, name='list_customer'),
    path('list_products/',views.list_products,name='list_products'),
    path('cart', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),

    path('detail_viwe/<int:id>', views.detail_viwe ,name='detail_viwe'),
    path('create/order/', views.create_order, name="create_order"),
    #path('search_poducts/<str:id>', views.search_poducts, name='search_poducts'),

    path('detail_viwe/<int:id>/', views.detail_viwe ,name='detail_viwe'),
    path('search_poducts', views.search_poducts, name='search_poducts'),
    path('', TemplateView.as_view(template_name='greeting.html')),

    
]    