from django.db import models

class Tile(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=300)

    def __str__(self):
        return "%s, %s - %s" % (self.title, self.date, self.content)
