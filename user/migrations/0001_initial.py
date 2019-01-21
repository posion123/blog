# Generated by Django 2.1.4 on 2019-01-11 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=150)),
                ('crate_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
