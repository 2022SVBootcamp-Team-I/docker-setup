# Generated by Django 3.2.14 on 2022-07-22 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_alter_image_fish'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Fish_info',
            new_name='Fish',
        ),
    ]
