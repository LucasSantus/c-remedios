# Generated by Django 3.1.6 on 2021-12-01 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20211201_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cidade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cidade_UsuarioFK', to='usuarios.cidade'),
        ),
    ]