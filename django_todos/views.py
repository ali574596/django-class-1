from django.shortcuts import HttpResponse
from django.http import JsonResponse


def home(request):
    context = {
        "name" : "john doe",
        "age" : 22
    }
    return JsonResponse(context, safe=False)