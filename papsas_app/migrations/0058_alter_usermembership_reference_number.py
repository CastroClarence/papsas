# Generated by Django 5.1.2 on 2024-10-17 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papsas_app', '0057_alter_candidacy_candidacystatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermembership',
            name='reference_number',
            field=models.BigIntegerField(null=True),
        ),
    ]