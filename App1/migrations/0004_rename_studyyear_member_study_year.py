# Generated by Django 4.1 on 2023-01-13 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0003_remove_member_year_member_studyyear'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='studyyear',
            new_name='study_year',
        ),
    ]