# Generated by Django 5.0.7 on 2024-09-19 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papsas_app', '0036_election_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verification_code_expiration',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]