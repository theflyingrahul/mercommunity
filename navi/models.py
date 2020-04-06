from django.db import models

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