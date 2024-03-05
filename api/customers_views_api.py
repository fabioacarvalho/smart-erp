from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from customers.models import *
from customers.serializers import *


class CustomersViewSet(APIView):
    def get(self, request, format=None):
        return Response(CustomerSerializer())

    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
