from django.http import JsonResponse

def hello(request):
    return JsonResponse({"message": "Hello from Django"})

def hai(request):
    return JsonResponse({"message": "Hai from Django"})
from django.shortcuts import render

# Create your views here.
