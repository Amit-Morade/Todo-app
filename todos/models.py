from django.db import models

# Create your models here.

class Todo(models.Model):
    content = models.TextField(max_length=250)

    def __str__(self):
        return self.content