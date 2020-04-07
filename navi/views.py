from django.shortcuts import render
from navi.models import File as file1

# Create your views here.

def index(request):
    return render(request, "navi/index.html")

def privilege(request):
    return render(request, "navi/admin.html")

def merlan(request):
    file = file1.objects.all()
    print(str(file))
    return render(request, "navi/merlan.html", {'files': file})