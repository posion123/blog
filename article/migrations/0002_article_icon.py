# Generated by Django 2.1.4 on 2019-01-26 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='icon',
            field=models.ImageField(null=True, upload_to='upload'),
        ),
    ]
