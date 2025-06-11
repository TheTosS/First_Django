from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    text = "<ol><ul><li>Welcome!</li></ul></ol>"
    return HttpResponse(text)

def about(request):
    text = "<h1>About Page</h1>"
    return HttpResponse(text)
