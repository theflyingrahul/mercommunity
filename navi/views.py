from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "navi/index.html")

def privilege(request):
    return render(request, "navi/admin.html")

def merlan(request):
    return render(request, "navi/merlan.html")