
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import productserializer
from .models import Product
@api_view(['GET'])
def api_overview(request):
    api_urls={
        'List': '/product-list/',
        'Detail view': '/product-detail/<int:id>',
        'create': '/product-create/',
        'Update': '/product-Update/<int:id>',
        'Delete': '/product-Delete/<int:id>',

    }
    return Response(api_urls)
@api_view(['GET'])
def showall(request):
    products=Product.objects.all()
    serializer=productserializer(products,many=True)#serialization
    return Response(serializer.data)

# @api_view(['GET'])
# def proddelete(request,product_id):
#     products=Product.objects.get(id=product_id)
#     products.delete()


#SingleProductView
@api_view(['GET'])
def singleprodview(request,pk):
    product=Product.objects.get(id=pk)
    #select * from product where id=2
    serializer=productserializer(product,many=False)
    return Response(serializer.data)
    
@api_view(['POST'])
def Createproduct(request):
    serializer=productserializer(data=request.data)# deserialization
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def singleprodview(request,pk):
    product=Product.objects.get(id=pk)
    serializer=productserializer(product,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def Updateproduct(request,pk):
    product=Product.objects.get(id=pk)
    #select * from product where id=3
    serializer=productserializer(instance=product,data=request.data) 
    if serializer.is_valid():
        serializer.save()
    return Response("updated")

@api_view(['GET'])
def Deleteproduct(request,pk):
    product=Product.objects.get(id=pk) 
     #select * from product where id=3
    product.delete()
    return Response("Successfully Deleted product")