# Generated by Django 3.1.6 on 2021-04-08 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_auto_20210408_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='data_inicio',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data de Ínicio:'),
        ),
    ]