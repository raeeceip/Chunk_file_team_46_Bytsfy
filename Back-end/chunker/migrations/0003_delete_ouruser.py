# Generated by Django 4.0.6 on 2022-08-14 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chunker', '0002_ouruser_delete_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OurUser',
        ),
    ]
