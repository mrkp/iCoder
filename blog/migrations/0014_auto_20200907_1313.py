# Generated by Django 3.1 on 2020-09-07 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200907_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(default='', upload_to='blog_image/'),
        ),
    ]
