# Generated by Django 4.1 on 2024-03-30 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_postphoto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='active',
        ),
    ]
