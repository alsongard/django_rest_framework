"""
One can have multiple serializers than 1:
example:
- one for discoount
- one for higher purchase

Also we can create another serializer that is going for submission of product_dta
"""
from django import forms
from rest_framework import serializers
from .models import ProductSchema
class ProductDiscountSerializer(serializers.ModelSerializer):
    sale_price = serializers.ReadOnlyField()
    class Meta:
        model = ProductSchema # reference the model and not instantiate it
        fields = [
            'title',
            "price",
            "description",
            "available",
            "remaining",
            "category" ,
            "sale_price"      
        ]

class ProductHigherPurchaseSerializer(serializers.ModelSerializer):
    higher_purchase = serializers.ReadOnlyField()
    class Meta:
        model = ProductSchema # reference the model and not instantiate it
        fields = [
            'title',
            "price",
            "description",
            "available",
            "remaining",
            "category" ,
            "higher_purchase"      
        ]



class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta: # defines custom interation with the database 
        model = ProductSchema # only reference the model and not instantiate it
        fields = [
            'title',
            "price",
            "description",
            "available",
            "remaining",
            "category" ,
        ]

# your normal productserializer
class ProductSerializer(serializers.ModelSerializer):
    model = ProductSchema
    class Meta:
        fields = [
            'title',
            "price",
            "description",
            "available",
            "remaining",
            "category",            
        ]