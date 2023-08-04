from django.db import models


# Create your models here.
class place(models.Model):
    objects = None
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pic')
    disc = models.TextField(null=True)

    def __str__(self):
        return self.name

class team(models.Model):
    objects = None
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='photos')
    disc = models.TextField(null=True)

    def __str__(self):
        return self.name
