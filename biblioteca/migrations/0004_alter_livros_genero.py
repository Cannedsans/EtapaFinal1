# Generated by Django 5.1.4 on 2025-01-26 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0003_alter_livros_sub_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='genero',
            field=models.CharField(max_length=20),
        ),
    ]
