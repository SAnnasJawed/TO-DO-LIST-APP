from django.db import models


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    done = models.BooleanField(default=False, null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
