from django.shortcuts import render
from django.http import JsonResponse
import json


# Create your views here.
def home_api(request, *args, **kwargs):
    data = {}
    
    print("request.body")
    print(request.body) # a byte string of json b''
    print("request.GET")
    print(request.GET)

    body = request.body

    try:
        data = json.loads(body)
    except: 
        pass
    print(f'this is data: {data}')
    return JsonResponse({"message":"Today is another day thankyou Lord for your mercies!"})
