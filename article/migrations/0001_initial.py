# Generated by Django 2.1.4 on 2019-01-18 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10, verbose_name='标题')),
                ('content', models.TextField()),
                ('desc', models.CharField(max_length=20, verbose_name='标题')),
                ('s_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='ChildTechnology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=20)),
                ('c_alias', models.CharField(max_length=20)),
                ('c_desc', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'child_technology',
            },
        ),
        migrations.CreateModel(
            name='FatherTechnology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=20, null=True)),
                ('f_alias', models.CharField(max_length=20)),
                ('f_desc', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'father_technology',
            },
        ),
        migrations.AddField(
            model_name='childtechnology',
            name='f',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.FatherTechnology'),
        ),
        migrations.AddField(
            model_name='article',
            name='child',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.ChildTechnology'),
        ),
        migrations.AddField(
            model_name='article',
            name='father',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.FatherTechnology'),
        ),
    ]
