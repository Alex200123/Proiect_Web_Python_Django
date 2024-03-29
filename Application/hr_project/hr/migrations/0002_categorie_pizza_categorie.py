# Generated by Django 4.1.4 on 2023-10-28 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nume', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Categorie',
                'db_table': 'categorie',
            },
        ),
        migrations.CreateModel(
            name='Pizza_categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('Categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.categorie')),
                ('Pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.pizza')),
            ],
            options={
                'verbose_name_plural': 'Pizza Categorie',
                'db_table': 'pizza_categorie',
            },
        ),
    ]
