# Generated by Django 5.1.2 on 2024-11-04 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papsas_app', '0063_alter_eventregistration_receipt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='pubmat',
            field=models.ImageField(blank=True, upload_to='papsas_app/pubmat/achievement'),
        ),
        migrations.AlterField(
            model_name='event',
            name='pubmat',
            field=models.ImageField(blank=True, upload_to='papsas_app/pubmat/event'),
        ),
        migrations.AlterField(
            model_name='membershiptypes',
            name='pubmat',
            field=models.ImageField(upload_to='papsas_app/pubmat/event'),
        ),
        migrations.AlterField(
            model_name='newsandoffers',
            name='pubmat',
            field=models.ImageField(blank=True, upload_to='papsas_app/pubmat/newsandoffers'),
        ),
    ]