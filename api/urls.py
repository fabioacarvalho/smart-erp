from django.urls import path, include
from api.customers_views_api import *

urlpatterns = [
    path('customers/', CustomersViewSet.as_view(), name='customers'),
]
