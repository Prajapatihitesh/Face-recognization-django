# Generated by Django 4.0.4 on 2022-10-07 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_delete_attendance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='contanct',
            new_name='contact',
        ),
    ]
