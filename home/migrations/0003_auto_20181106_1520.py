# Generated by Django 2.0.6 on 2018-11-06 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20181106_1515'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='autor',
            new_name='author',
        ),
    ]
