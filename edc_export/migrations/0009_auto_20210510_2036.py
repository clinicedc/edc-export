# Generated by Django 3.2 on 2021-05-10 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edc_export', '0008_auto_20201002_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exportdata',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='importdata',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
