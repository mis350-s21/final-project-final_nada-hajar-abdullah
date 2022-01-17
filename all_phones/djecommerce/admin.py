from django.contrib import admin
from .models import Customer,Product,Order

# Register your models here.
class productInLine(admin.TabularInline):
  model=Product


admin.site.register(Customer)
inlines = (productInLine,)
admin.site.register(Product)
#admin.site.register(feedback)

admin.site.register(Order)
