# requests

To send a request to an api(think as a url) you use the ``requests`` module.
```py
import requests
```

Setting a variable as such:
```py
my_url = "http://google.com"
my_response = requests.get(my_url).text
print(my_response)


```
The above is a normal http request


When sending a REST http request your response is in JSON
Example:


```json
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate, br, zstd", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.32.5", 
    "X-Amzn-Trace-Id": "Root=1-68de3913-12aebc944176eed91421792a"
  }, 
  "json": null, 
  "method": "GET", 
  "origin": "41.90.41.255", 
  "url": "https://httpbin.org/anything"
}
```


```py
another_repsonse = requests.get("https://httpbin.org/anything", data={"query":"Hello World"})

print("another_repsonse")
print(another_repsonse.json())


another_repsonse_with_json = requests.get("https://httpbin.org/anything", json={"query":"Hello World"})
print("another_response_with_json")
print(another_repsonse_with_json.json())


# you can also get the status code of a response
print(another_repsonse_with_json.status_code)
```

An example of sending data from the backendin httpResponse is:
```py
def home_api_view(request, *args, **kwargs):
    return JsonResponse({"property_name":"value"})
```
```py
my_response = requests.get("http://localhost:8000/api")
print(my_response.json())
print(my_response.status_code)
print(my_response.json()["message"])
```

## getting data from dbsqlite3
