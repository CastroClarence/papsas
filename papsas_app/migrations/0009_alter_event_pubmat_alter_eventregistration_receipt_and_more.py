# Generated by Django 5.0.7 on 2024-09-02 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papsas_app', '0008_alter_user_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='pubmat',
            field=models.ImageField(null=True, upload_to='papsas_app/pubmat'),
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='receipt',
            field=models.ImageField(blank=True, null=True, upload_to='papsas_app/reciept'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profilePic',
            field=models.ImageField(blank=True, null=True, upload_to='papsas_app/profilePic'),
        ),
    ]