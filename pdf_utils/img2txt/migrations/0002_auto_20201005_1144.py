# Generated by Django 3.1.2 on 2020-10-05 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('img2txt', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='picture',
            new_name='image',
        ),
    ]
