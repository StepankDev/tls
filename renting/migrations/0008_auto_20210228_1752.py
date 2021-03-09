# Generated by Django 3.1.6 on 2021-02-28 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('renting', '0007_rentplace_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentplace',
            name='district',
        ),
        migrations.AddField(
            model_name='rentplace',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='renting.district'),
        ),
    ]