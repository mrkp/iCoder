# Generated by Django 3.1 on 2020-09-06 08:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='timestamp',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
