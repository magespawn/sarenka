# Generated by Django 3.1.7 on 2021-07-19 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vulnerabilities', '0009_remove_cve_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpe',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vector',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
