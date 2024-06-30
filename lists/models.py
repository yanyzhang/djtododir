from django.db import models


# Create your models here.
class Lists (models.Model):

    title=models.CharField(max_length=255)
    image=models.ImageField(upload_to='images/')
    description=models.CharField(max_length=1000)

    def __str__(self):
        return self.title


class Todolistmdl (models.Model):
    text = models.CharField(max_length=200)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    completed=models.BooleanField(default=False)
    

    def __str__(self):
        return self.text