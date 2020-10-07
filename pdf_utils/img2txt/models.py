from django.db import models

from secrets import token_hex

# Create your models here.


def create_task_id():
    while True:
        hex = token_hex(10)
        if Image.object.get(task_id=hex) == '':
            task_id = hex
            break
    return task_id


class Image(models.Model):
    task_id = models.CharField(max_length=40)
    image = models.ImageField(upload_to='img2txt/'+create_task_id())

    def __str__(self):
        return self.task_id
