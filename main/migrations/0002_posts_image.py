# Generated by Django 3.1.2 on 2020-10-26 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='Image',
            field=models.ImageField(default='default.jpg', upload_to='blog_pics'),
        ),
    ]
