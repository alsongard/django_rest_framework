from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import ProductSchema
from .serializers import ProductSerializer



# when working with generics we must use a class
"""
class ClassNameGenericUseCaseView(generics.USECASE_VIEW)
**note**there are multiple views check: [link]()
"""
class ProductDetailViewAPI(generics.RetrieveAPIView):
    # get data
    queryset = ProductSchema.objects.all()
    serializer_class = ProductSerializer
    
