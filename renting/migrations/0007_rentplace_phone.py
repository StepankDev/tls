# Generated by Django 3.1.6 on 2021-02-28 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renting', '0006_auto_20210228_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentplace',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
