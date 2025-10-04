import requests


my_endpoint = "https://httpbin.org/"

my_response = requests.get(my_endpoint).text

# print(my_response)



# second url : awkward response
# second_url = "https://google.com"

# my_second_response = requests.get(second_url).text
# print("my_second_response")
# print(my_second_response)

second_url = "https://httpbin.org/anything"
my_second_response = requests.get(second_url)
# print(my_second_response.text)


# convert to json format
# print(my_second_response.json())


# one can pass data to the url/api in the format below:
"""

reqeusts.get("url", json={"query":"Hello world"})
"""
 

another_repsonse = requests.get("https://httpbin.org/anything", data={"query":"Hello World"})

print("another_repsonse")
print(another_repsonse.json())
# using data the Content-Type is set to form-url-encoded

another_repsonse_with_json = requests.get("https://httpbin.org/anything", json={"query":"Hello World"})

print("another_response_with_json")
# print(another_repsonse_with_json.json())


# you can also get the status code of a response
# print(another_repsonse_with_json.status_code)



# getting api from backend
my_response = requests.get("http://localhost:8000/api", params={"product_id": 23}, json={"product_name":"smart phone"})
# print(my_response.json())
print(my_response.status_code)

print(my_response.json())\


create_product = requests.post('http://localhost:8000/api/createProduct', json={
    'title':"DELL  Laptop Latitude E7450",
    "price": 80000,
    "description": "512GB storage, 16Gb RAM",
    "available": True,
    "remaining": 4,
    "category":"Electronics"
    }
    )

print("create_product")
print(create_product)


