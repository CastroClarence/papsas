# Generated by Django 5.0.7 on 2024-08-31 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papsas_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='eventDate',
            new_name='endDate',
        ),
        migrations.AddField(
            model_name='event',
            name='startDate',
            field=models.DateField(null=True),
        ),
    ]
