from django.contrib import admin
from customers.models import *

admin.site.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email', 'phone', 'address', 'password', 'city', 'country', 'is_active',)
    list_filter = ('user', 'first_name', 'last_name', 'email', 'phone', 'address', 'password', 'city', 'country', 'is_active',)
    search_fields = ('user', 'first_name', 'last_name', 'email', 'phone', 'address', 'password', 'city', 'country', 'is_active',)
    # fieldsets = (
    #     ('Seção 1', {
    #         'fields': ('user', 'first_name', 'last_name', 'email', 'phone', 'address', 'password', 'city', 'country', 'is_active',),
    #     }),
    # )
    #
    # list_per_page = 10