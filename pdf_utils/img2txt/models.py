from django.db import models

# Create your models here.


class Image(models.Model):
    task_id = models.CharField(max_length=40)
    image = models.ImageField(upload_to='img2txt/')

    def __str__(self):
        return self.task_id
