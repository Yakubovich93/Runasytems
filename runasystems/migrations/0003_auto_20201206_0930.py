# Generated by Django 3.1.4 on 2020-12-06 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runasystems', '0002_auto_20201206_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
