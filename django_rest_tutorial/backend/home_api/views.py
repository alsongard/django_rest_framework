from django.shortcuts import render
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from products.models import ProductSchema
from products.serializers import ProductSerializer,ProductHigherPurchaseSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# working with rest_framework

# Create your views here.
def home_api(request, *args, **kwargs):

    product = ProductSchema.objects.get(id=1)
    print(f'this is product:\n ${product}')

    data = {}

    # if product:
    #     data["id"] = product.id,
    #     data["title"] = product.title,
    #     data["price"] = product.price,
    #     data["description"] = product.description,
    #     data["available"] = product.available,
    #     data["remaining"] = product.remaining,
    #     data["category"] = product.category

    if product:
        # instead of the above which is manual, we can use model_to_dict() method
        data = model_to_dict(product, fields=["id", "title", "price"])
        # one can also specify the fields which he/she wants
    
    print("request.body")
    print(request.body) # a byte string of json b''
    print("request.GET")
    print(request.GET)

    body = request.body

    try:
        data = json.loads(body)
    except: 
        pass
    print(f'this is data: {data}')
    return JsonResponse({"message":"Today is another day thankyou Lord for your mercies!", "productFound":data})


# so the JsonResponse form http takes json objects that is:
"""
JsonResponse({"objectProperty": "objectValue"})

"""


# to use django rest_framework_api we import the following: 
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
"""

@api_view(["GET"])
def product_get_view(reqeust, *args, **kwargs):
    found_product = ProductSchema.objects.get(id=1)
    # if found_product == None:
    #     return JsonResponse({"success":False, "msg":"No products found"})
    # data = model_to_dict(found_product)
    print("found_product")
    print(found_product)

    # .data is a method 
    if found_product:
        data = ProductSerializer(found_product).data
        return Response(data)

@api_view(["GET"])
def get_with_higher_purchase(request, *args, **kwargs):
    found_product = ProductSchema.objects.get(id=1)

    print("found_product")
    print(found_product)

    # .data is a method 
    if found_product:
        data = ProductHigherPurchaseSerializer(found_product).data
        return Response(data)