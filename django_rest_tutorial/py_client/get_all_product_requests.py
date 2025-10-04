import requests


my_products = requests.get("http://localhost:8000/api")

print("my_products")
print(my_products)


print(my_products.json())
