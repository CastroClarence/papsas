# Generated by Django 5.1.2 on 2024-10-15 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papsas_app', '0052_alter_user_options_eventrating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='election',
            options={'ordering': ['id']},
        ),
    ]
