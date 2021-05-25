from django.db import models
from django.utils import timezone
from django.conf import settings


class Comparison(models.Model):
    obj1 = models.CharField(max_length=256)
    obj2 = models.CharField(max_length=256)
    obj1_count = models.IntegerField()
    obj2_count = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)


class Comment(models.Model):
    obj1 = models.CharField(max_length=256)
    obj2 = models.CharField(max_length=256)
    is_obj1 = models.BooleanField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)