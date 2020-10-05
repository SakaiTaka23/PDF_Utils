from django.db import models

# Create your models here.


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    task_id = models.CharField(unique=True, null=True)

    def __str__(self):
        return self.title
