from django.db import models

# Create your models here.

class Photoes(models.Model):
    title = models.CharField(max_length=20, null=False, unique=True)
    content = models.FileField(null=True)
    desc = models.CharField(max_length=20, null=True)
    p_time = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'photo'
