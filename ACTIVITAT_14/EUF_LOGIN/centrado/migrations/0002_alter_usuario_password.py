# Generated by Django 4.2.19 on 2025-05-05 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centrado', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
