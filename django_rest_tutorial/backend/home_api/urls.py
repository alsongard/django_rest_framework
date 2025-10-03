from django.urls import path
from .views import home_api, product_get_view, get_with_higher_purchase


urlpatterns = [
    path("",home_api),
    path("get_product/", product_get_view, name='product_view'),
    path("get_product_higher_purchase",get_with_higher_purchase, name="the_higher" )
]