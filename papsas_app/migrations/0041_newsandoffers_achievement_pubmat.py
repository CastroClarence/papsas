# Generated by Django 5.0.7 on 2024-09-25 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papsas_app', '0040_election_numwinners'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsandOffers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, null=True)),
                ('description', models.TextField(max_length=9999, null=True)),
                ('postStamp', models.DateTimeField(auto_now_add=True)),
                ('pubmat', models.ImageField(null=True, upload_to='papsas_app/pubmat/newsandoffers')),
            ],
        ),
        migrations.AddField(
            model_name='achievement',
            name='pubmat',
            field=models.ImageField(null=True, upload_to='papsas_app/pubmat/achievement'),
        ),
    ]
