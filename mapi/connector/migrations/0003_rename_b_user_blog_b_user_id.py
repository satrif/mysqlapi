# Generated by Django 3.2.6 on 2021-09-04 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connector', '0002_auto_20210904_2344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='B_User',
            new_name='B_User_id',
        ),
    ]
