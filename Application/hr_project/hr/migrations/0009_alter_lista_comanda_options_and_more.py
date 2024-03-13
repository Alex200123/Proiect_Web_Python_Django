# Generated by Django 4.2.1 on 2023-11-19 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0008_delete_transaction_alter_lista_comanda_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lista_comanda',
            options={'verbose_name_plural': 'Lista Comenzi'},
        ),
        migrations.AlterField(
            model_name='cos_cumparaturi',
            name='Pizza',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='hr.pizza'),
        ),
    ]
