# Generated by Django 3.1.2 on 2020-10-22 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubeSection', '0002_auto_20201022_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtubesection',
            name='description',
            field=models.TextField(blank=True, max_length=5000),
        ),
    ]
