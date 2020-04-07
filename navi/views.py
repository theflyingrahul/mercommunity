import os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from navi.models import File as file1
import datetime


# Create your views here.

def index(request):
    return render(request, "navi/index.html")

def privilege(request):
    return render(request, "navi/admin.html")

def merlan(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['uploaded_file']
        print(uploaded_file.size)
        fs = FileSystemStorage()
        stored_name = fs.save(uploaded_file.name, uploaded_file)
        ext = os.path.splitext(uploaded_file.name)[1].upper().lstrip('.')
        file_object = file1(name=uploaded_file.name[0:48], fmt=ext, uploaded_by="rah", file_size=int(uploaded_file.size/1024/1024), date_time=datetime.datetime.now(), url=stored_name)
        file_object.save()
    file_query = file1.objects.all()
    return render(request, "navi/merlan.html", {'files': file_query})