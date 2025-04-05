from django.shortcuts import render
from .models import Product
from rest_framework.response import Response
from rest_framework import generics
from .serializers import ProductSerializer

class ProductOperationsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()  # Ensure Product model exists and is migrated
    serializer_class = ProductSerializer  # Ensure ProductSerializer is correctly defined
    lookup_field = 'id'  # Ensure the field used for lookups is correct


class ProductListAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()  # Ensure Product model exists and is migrated
    serializer_class = ProductSerializer  # Ensure ProductSerializer is correctly defined
    
    
    # def perform_create(self, serializer):

    #     """
    #     When you use perform_create or ModelViewSet and follow post requires, Perform_create is called.

    #     Virtual Perform_create works like that:

    #     def perform_create(self, serializer):
    #         name = serializer.validate_data.get('name')
    #         description = serializer.validate_data.get('description')
    #         serializer.save()
    
    #     """
    #     return super().perform_create(serializer)