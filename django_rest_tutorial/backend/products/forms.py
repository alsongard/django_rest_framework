from django import forms

from .models import ProductSchema
class ProductForms(forms.ModelForm):
    class Meta:
        model = ProductSchema
        fields = [
            'title',
            "price",
            "description",
            "available",
            "remaining",
            "category"       
        ]