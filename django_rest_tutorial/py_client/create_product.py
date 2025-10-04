import requests

the_response = requests.post("http://localhost:8000/api/createProduct/", {
    "title":"Lamborghini Venon",
    "price": 2000000,
    "description": "15000 horse power and 20 litre oil tank. 0 to 120m per second",
    "available": "True",
    "remaining": 10,
    "category": "Cars"
})

print('this is resposne')
print(the_response)

