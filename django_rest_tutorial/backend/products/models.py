from django.db import models
from decimal import Decimal

# Create your models here.
class ProductSchema(models.Model):
    PRODUCT_CHOICES = [
        ("ELECTRONICS", "Electronics"),
        ("FASHION", "Fashion"), 
        ("GROCERY", "Grocery"),
        ("HOME_APPLIANCES", "Home Appliances"),
        ("BOOKS", "Books"),
        ("TOYS", "Toys"),
        ("SPORTS", "Sports"),
        ("BEAUTY", "Beauty"),
        ("HEALTH", "Health"),
        ("AUTOMOTIVE", "Automotive"),
        ("MUSIC", "Music"),
        ("MOVIES", "Movies"),
        ("GAMES", "Games"),
        ("FURNITURE", "Furniture"),
        ("JEWELRY", "Jewelry"),
        ("CARS", "Cars"),
        ("OTHER", "Other"),
    ]
    title = models.CharField(max_length=120, default="")
    price = models.DecimalField(max_digits=15, null=False, blank=False, decimal_places=2, default=Decimal("99.11"))
    description = models.TextField(null=False, blank=False)
    available = models.BooleanField(default=True)
    remaining = models.IntegerField(default=10)
    category = models.CharField(choices=PRODUCT_CHOICES, max_length=100, default="Electronics")


    @property # this is used to set the method available as an attribute
    def sale_price(self):
        return "%.2f" %(float(self.price)*0.8)
    
    @property 
    def higher_purchase(self):
        higher_purchase = (0.1*float(self.price))
        return int(higher_purchase * 12) + self.price
         





