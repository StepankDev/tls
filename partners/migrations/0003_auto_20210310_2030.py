# Generated by Django 3.1.6 on 2021-03-11 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0002_partnerinfo_business_district'),
    ]

    operations = [
        migrations.AddField(
            model_name='partnerinfo',
            name='ruc',
            field=models.CharField(default=123, max_length=9),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='partnerinfo',
            name='document',
            field=models.CharField(max_length=200),
        ),
    ]
