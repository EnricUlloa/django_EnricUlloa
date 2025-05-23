# Generated by Django 4.2.19 on 2025-03-18 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('cognom1', models.CharField(max_length=100)),
                ('cognom2', models.CharField(blank=True, max_length=100, null=True)),
                ('correu', models.EmailField(max_length=254)),
                ('curs', models.CharField(max_length=50)),
                ('moduls_matriculats', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('cognom1', models.CharField(max_length=100)),
                ('cognom2', models.CharField(blank=True, max_length=100, null=True)),
                ('correu', models.EmailField(max_length=254)),
                ('curs', models.CharField(max_length=50)),
                ('tutor', models.BooleanField(default=False)),
                ('moduls_imparteix', models.TextField()),
            ],
        ),
    ]
