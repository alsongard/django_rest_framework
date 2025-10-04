import requests


foundProduct = requests.get("http://localhost:8000/api/get_product_higher_purchase")

print("foundProduct")
print(foundProduct)