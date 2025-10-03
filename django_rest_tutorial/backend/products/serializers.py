"""
One can have multiple serializers than 1:
example:
- one for discoount
- one for higher purchase

"""
from django import forms
from rest_framework import serializers
from .models import ProductSchema
class ProductSerializer(serializers.ModelSerializer):
    sale_price = serializers.ReadOnlyField()
    class Meta:
        model = ProductSchema
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
        model = ProductSchema
        fields = [
            'title',
            "price",
            "description",
            "available",
            "remaining",
            "category" ,
            "higher_purchase"      
        ]