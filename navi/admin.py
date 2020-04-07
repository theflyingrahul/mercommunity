from django.contrib import admin
from navi.models import User, UserGroup, File

# Register your models here.
admin.site.register(User)
admin.site.register(UserGroup)
admin.site.register(File)