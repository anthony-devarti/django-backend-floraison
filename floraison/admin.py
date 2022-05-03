from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(user_address)
admin.site.register(Order)
admin.site.register(category)
admin.site.register(cookie_type)
admin.site.register(cake_type)
admin.site.register(frosting)
admin.site.register(filling)
admin.site.register(item)
admin.site.register(order_item)