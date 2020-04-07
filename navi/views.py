from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from navi.models import File as file1


# Create your views here.

def index(request):
    return render(request, "navi/index.html")

def privilege(request):
    return render(request, "navi/admin.html")

def merlan(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['uploaded_file']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    file_query = file1.objects.all()
    return render(request, "navi/merlan.html", {'files': file_query})