# Generated by Django 5.1.2 on 2024-11-05 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papsas_app', '0065_alter_achievement_name_alter_event_eventname_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='achievement',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='newsandoffers',
            options={'ordering': ['id']},
        ),
    ]