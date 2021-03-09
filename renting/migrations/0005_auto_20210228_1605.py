# Generated by Django 3.1.6 on 2021-02-28 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renting', '0004_auto_20210228_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentplace',
            name='payment',
            field=models.ManyToManyField(related_name='payment_list', related_query_name='payment', to='renting.PaymentMode'),
        ),
    ]