# Generated by Django 3.1.7 on 2021-07-19 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vulnerabilities', '0011_auto_20210719_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpe',
            name='id',
            field=models.CharField(default='-1', max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vector',
            name='id',
            field=models.CharField(default='-1', max_length=50, primary_key=True, serialize=False),
        ),
    ]
