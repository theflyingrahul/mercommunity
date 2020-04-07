from django.shortcuts import render
from navi.models import File as file1

# Create your views here.

def index(request):
    return render(request, "navi/index.html")

def privilege(request):
    return render(request, "navi/admin.html")

def merlan(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['uploaded_file']
        print(uploaded_file.name)
        print(uploaded_file.size)
    file_query = file1.objects.all()
    return render(request, "navi/merlan.html", {'files': file_query})