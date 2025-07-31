from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello,This is our first django wedsite");
    return render(request,'index.html')
def about (request):
    return HttpResponse("hello,this is our about page")
    return HttpResponse("Hello, This is our contact page")
def contact (request):
    return HttpResponse("hello,this is our contact page")
    return HttpResponse("Hello, This is our contact page")
