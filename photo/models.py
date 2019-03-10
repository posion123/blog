from django.db import models

# Create your models here.

class Photoes(models.Model):
    title = models.CharField(max_length=20, null=False, unique=True)
    content = models.FileField(null=True)
    desc = models.CharField(max_length=20, null=True)
    p_time = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'photo'

class Mfile(models.Model):
    title = models.CharField(max_length=100)
    name = models.FileField(upload_to='file2', null=True)
    time = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'my_file'
