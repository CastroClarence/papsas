# Generated by Django 5.0.7 on 2024-09-01 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papsas_app', '0005_event_price_eventregistration_receipt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='audience',
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='receipt',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='profilePic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
