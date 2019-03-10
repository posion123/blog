from django.db import models


class FatherTechnology(models.Model):
    f_name = models.CharField(max_length=20, null=True)
    f_alias = models.CharField(max_length=20)
    f_desc = models.CharField(max_length=20)
    class Meta:
        db_table = 'father_technology'

class ChildTechnology(models.Model):
    c_name = models.CharField(max_length=20)
    c_alias = models.CharField(max_length=20)
    f = models.ForeignKey(FatherTechnology, on_delete=models.CASCADE)
    c_desc = models.CharField(max_length=20)
    class Meta:
        db_table = 'child_technology'
class Article(models.Model):
    title = models.CharField(max_length=10, verbose_name='标题')
    content = models.TextField()
    desc = models.CharField(max_length=20, verbose_name='标题')
    s_time = models.DateTimeField(auto_now_add=True)
    child = models.ForeignKey(ChildTechnology, on_delete=models.CASCADE)
    father = models.ForeignKey(FatherTechnology, on_delete=models.CASCADE)
    icon = models.ImageField(upload_to='upload', null=True)
    class Meta:
        db_table = 'article'