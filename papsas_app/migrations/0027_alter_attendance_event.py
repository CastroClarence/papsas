# Generated by Django 5.0.7 on 2024-09-15 17:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papsas_app', '0026_remove_event_address_alter_event_venue_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='papsas_app.eventregistration'),
        ),
    ]
