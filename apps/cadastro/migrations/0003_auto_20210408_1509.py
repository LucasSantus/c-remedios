# Generated by Django 3.1.6 on 2021-04-08 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_auto_20210408_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='data_inicio',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Ínicio:'),
        ),
        migrations.AlterField(
            model_name='receita',
            name='dosagem',
            field=models.PositiveIntegerField(verbose_name='Dosagem:'),
        ),
    ]