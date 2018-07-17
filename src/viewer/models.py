from django.db import models
from django.contrib.auth.models import User


class Code(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.CharField(max_length=8, unique=True)
    source = models.TextField(blank=True)
    language = models.CharField(max_length=12, blank=True, default='python')
