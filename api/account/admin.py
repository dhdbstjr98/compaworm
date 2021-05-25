from django.contrib import admin
from .models import User, UserToken
from django.contrib.auth.models import Group

# Register your models here.

admin.site.register([User, UserToken])
admin.site.unregister(Group)