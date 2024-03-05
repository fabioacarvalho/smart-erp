from django.db import models
from base.models import *


class Customer(Person):
    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.first_name + " " + self.last_name
