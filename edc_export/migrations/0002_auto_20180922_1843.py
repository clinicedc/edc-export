# Generated by Django 2.1 on 2018-09-22 16:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("edc_export", "0001_initial")]

    operations = [
        migrations.AlterModelOptions(
            name="datarequesthistory",
            options={
                "ordering": ("-exported_datetime",),
                "verbose_name": "Data Request History",
                "verbose_name_plural": "Data Request History",
            },
        )
    ]
