# Generated by Django 5.0.7 on 2024-09-19 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papsas_app', '0037_user_verification_code_expiration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievementName', models.CharField(max_length=32, null=True)),
                ('achievementDescription', models.TextField(max_length=9999, null=True)),
                ('postStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='postStamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
