# Generated by Django 3.1.2 on 2020-10-23 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('title', models.CharField(max_length=255)),
                ('description1', models.TextField(blank=True, max_length=5000)),
                ('description2', models.TextField(blank=True, max_length=5000)),
                ('description3', models.TextField(blank=True, max_length=5000)),
                ('image', models.CharField(blank=True, default='default.jpg', max_length=1000)),
                ('link', models.CharField(blank=True, max_length=1000)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
