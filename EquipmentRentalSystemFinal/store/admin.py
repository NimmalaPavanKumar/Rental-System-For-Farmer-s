from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

# class ContactAdmin(admin.ModelAdmin):
#     list_display=('name', 'email', 'message')
# admin.site.register(Contact, ContactAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'message')
admin.site.register(Feedbacks, FeedbackAdmin)

class SupplierAdmin(admin.ModelAdmin):
    list_display=('first_name', 'lastname', 'gender', 'date_of_birth',
        'aadharnumber', 'email', 'phonenumber', 'address')
admin.site.register(Supplier, SupplierAdmin)