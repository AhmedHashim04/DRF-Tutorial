from django.shortcuts import render
from .models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def product_operations(request, *args, **kwargs):
    """
    Handles CRUD operations for products based on the HTTP request method.
    Args:
        request: The HTTP request object containing method and data.
        *args: Additional positional arguments. (tuble)
        **kwargs: Additional keyword arguments, such as 'id' for specific product operations.(dict)
    Returns:
        Response: A DRF Response object containing serialized data or a success message.
    Supported Methods:
        - GET: Retrieves all products and returns them as serialized data.
        - POST: Creates a new product using the data provided in `request.data`.
        - DELETE: Deletes a product identified by 'id' in `kwargs`.
        - PUT: Updates a product identified by 'id' in `kwargs` using the data in `request.data`.
    Note:
        - The `request.data` is used for POST, DELETE, and PUT operations instead of relying solely on `kwargs`.
    """
    if request.method == 'GET':
        products = Product.objects.all()  # Get all products
        # products = Product.objects.all().order_by('?')[:5]  # Get a random list of 5 products
        serialized_products = ProductSerializer(products, many=True).data
        return Response({'products': serialized_products})
    
    if request.method == 'POST':
        product_serializer = ProductSerializer(data=request.data)
        print(request.data)
        if product_serializer.is_valid(raise_exception=True):
            product_serializer.save()
            return Response(product_serializer.data)

    if request.method == 'DELETE':
        print(request.data)
        product = Product.objects.get(id=kwargs['id'])
        # print(request.data['id'][0])
        product.delete()
        return Response({'message': 'Product deleted successfully'})
    
    if request.method == 'PUT':
        product = Product.objects.get(id=kwargs['id'])
        updated_data = ProductSerializer(product, data=request.data)

        if updated_data.is_valid(raise_exception=True):
            updated_data.save()
            return Response(updated_data.data)
