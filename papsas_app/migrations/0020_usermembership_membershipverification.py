# Generated by Django 5.0.7 on 2024-09-08 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papsas_app', '0019_usermembership_verificationid'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermembership',
            name='membershipVerification',
            field=models.BooleanField(default=False),
        ),
    ]
