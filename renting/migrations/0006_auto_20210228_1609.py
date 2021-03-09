# Generated by Django 3.1.6 on 2021-02-28 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('renting', '0005_auto_20210228_1605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentplace',
            name='payment',
        ),
        migrations.AddField(
            model_name='rentplace',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='renting.paymentmode'),
        ),
    ]
