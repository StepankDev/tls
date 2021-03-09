# Generated by Django 3.1.6 on 2021-02-28 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renting', '0002_auto_20210228_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='rentplace',
            name='payment_mode',
            field=models.ManyToManyField(to='renting.PaymentMode'),
        ),
    ]