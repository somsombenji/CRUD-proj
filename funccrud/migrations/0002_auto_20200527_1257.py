# Generated by Django 3.0.6 on 2020-05-27 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funccrud', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='pub_title',
            new_name='pub_date',
        ),
    ]
