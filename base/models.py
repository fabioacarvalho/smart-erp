from django.db import models
from django.contrib.auth.models import User


class Person(User):
    phone = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    country = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
