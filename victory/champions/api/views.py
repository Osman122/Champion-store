from rest_framework.response import Response
from rest_framework.decorators import api_view

from champions.models import Product
from champions.api.serializers import ProductSerializer



@api_view(['GET', 'POST'])
def indexx(request):
    if request.method == 'POST':
        product = ProductSerializer(data=request.data)
        if product.is_valid():
            product.save()
            return Response({"messsage": 'object add received', "student":product.data}, status=201)
        return Response(product.errors, status=400)

    elif request.method=='GET':
        products = Product.get_all()  # query set of model objects
        serlized_products = ProductSerializer(products, many=True)
        return Response({"message": "students data receieved", 'students': serlized_products.data})




### operations on specific object


@api_view(['GET', 'DELETE', 'PUT'])
def product_resource(request, id):
    product = Product.objects.filter(id=id).first()
    if request.method=='GET':
        product = Product.objects.filter(id=id).first()
        serlized_Product = ProductSerializer(product)
        return Response({'data':serlized_Product.data}, status=200)

    elif request.method=='DELETE':
        product.delete()
        return Response({"message":"object deleted"}, status= 204)

    elif request.method=="PUT":
        serlized_product = ProductSerializer(instance=product,data=request.data)
        if serlized_product.is_valid():
            serlized_product.save()
            return Response({"messsage": 'object add received', "student": serlized_product.data}, status=201)
        return Response(serlized_product.errors, status=400)

