from django.db import models

class Tile(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True, auto_now_add=True)
    content = models.CharField(max_length=300)
