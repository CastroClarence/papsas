# Generated by Django 5.0.7 on 2024-09-07 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papsas_app', '0015_remove_user_memtype_alter_membershiptypes_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermembership',
            name='receipt',
            field=models.ImageField(blank=True, null=True, upload_to='papsas_app/reciept'),
        ),
    ]