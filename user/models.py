from django.db import models

class User(models.Model):
    s_name = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=150, null=False)
    crate_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'
