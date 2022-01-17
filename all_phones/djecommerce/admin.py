from django.contrib import admin
from .models import Customer,Product,feedback

# Register your models here.
class productInLine(admin.TabularInline):
  model=Product


admin.site.register(Customer)
inlines = (productInLine,)
admin.site.register(Product)
admin.site.register(feedback)
