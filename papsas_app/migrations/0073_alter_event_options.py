# Generated by Django 5.1.2 on 2024-11-26 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papsas_app', '0072_alter_usermembership_receipt_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-startDate']},
        ),
    ]