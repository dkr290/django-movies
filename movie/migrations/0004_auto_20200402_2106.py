# Generated by Django 3.0.2 on 2020-04-02 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20200402_2046'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movie_Links',
            new_name='MovieLinks',
        ),
    ]
