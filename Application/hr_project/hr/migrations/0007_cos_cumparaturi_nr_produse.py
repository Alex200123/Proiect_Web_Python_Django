# Generated by Django 4.2.1 on 2023-11-18 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0006_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='cos_cumparaturi',
            name='nr_produse',
            field=models.DecimalField(decimal_places=0, default=20, max_digits=4),
        ),
    ]