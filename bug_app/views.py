from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    print("输出代码信息")
    return HttpResponse("index")