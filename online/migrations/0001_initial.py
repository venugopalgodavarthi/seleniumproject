# Generated by Django 4.0.5 on 2022-06-30 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='universitymodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='collegemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('noofstudents', models.IntegerField()),
                ('website', models.URLField()),
                ('email', models.EmailField(max_length=254)),
                ('noofstaff', models.IntegerField()),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online.universitymodel')),
            ],
        ),
    ]
