# Generated by Django 5.0.1 on 2024-02-24 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0004_rename_abouthead_about_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='aboutdescription',
            new_name='Des',
        ),
    ]