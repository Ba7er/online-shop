from django.contrib import admin
from .models import Cart , ShippingAddresses , My_order
# Register your models here.
admin.site.register(Cart)

admin.site.register(ShippingAddresses)
admin.site.register(My_order)
