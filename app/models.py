from django.db import models


# Create your models here.


class Message(models.Model):
    name = models.CharField(max_length=20, null=False)
    email = models.EmailField(null=True)
    content = models.TextField(null=True)
    answer = models.TextField(null=True)
    time = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'message'
