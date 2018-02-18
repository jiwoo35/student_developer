# Generated by Django 2.0.1 on 2018-01-28 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='content',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='photo',
            name='filtered_image',
            field=models.ImageField(upload_to='uploads/%Y/%m/%d/filtered'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='uploads/%Y/%m/%d/orig'),
        ),
    ]
