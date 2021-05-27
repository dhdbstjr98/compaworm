from django.db import models
from django.utils import timezone
from django.conf import settings


class Comparison(models.Model):
    obj1 = models.CharField(max_length=256, null=False)
    obj2 = models.CharField(max_length=256, null=False)
    is_obj1 = models.BooleanField(null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)


class Comment(models.Model):
    obj1 = models.CharField(max_length=256, null=False)
    obj2 = models.CharField(max_length=256, null=False)
    is_obj1 = models.BooleanField(null=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField(null=False)
    created_at = models.DateTimeField(default=timezone.now)
