from django.db import models

# Create your models here.


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    task_id = models.CharField(max_length=40)

    def __str__(self):
        return self.task_id
