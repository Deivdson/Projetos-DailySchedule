# Generated by Django 3.2.3 on 2022-08-15 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulado', '0002_auto_20220815_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resposta',
            name='texto',
            field=models.TextField(verbose_name='texto'),
        ),
        migrations.AlterField(
            model_name='simulado',
            name='titulo',
            field=models.CharField(max_length=20, verbose_name='título'),
        ),
    ]
