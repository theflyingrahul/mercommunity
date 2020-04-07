from django.db import models
import datetime
# Create your models here.

class UserGroup(models.Model):
    dept = models.CharField(max_length=5)
    year = models.IntegerField()

    def __str__(self):
        return self.dept+"-"+str(self.year)

class User(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=30)
    group = models.ForeignKey(UserGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.username+" : "+self.password +" in "+str(self.group)

class File(models.Model):
    name = models.CharField(max_length=50)
    file_size = models.IntegerField()
    uploaded_by = models.CharField(max_length=30)
    date_time = models.DateTimeField(default=datetime.datetime.now)
    url = models.CharField(max_length=500)

    def __str__(self):
        return self.name+" "+str(self.file_size)