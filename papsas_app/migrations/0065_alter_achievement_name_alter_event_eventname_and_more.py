# Generated by Django 5.1.2 on 2024-11-05 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papsas_app', '0064_alter_achievement_pubmat_alter_event_pubmat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventName',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='newsandoffers',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]