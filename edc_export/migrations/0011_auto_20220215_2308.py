# Generated by Django 3.2.8 on 2022-02-15 21:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("edc_export", "0010_auto_20210910_1636"),
    ]

    operations = [
        migrations.AlterField(
            model_name="datarequest",
            name="export_format",
            field=models.CharField(
                choices=[
                    ("CSV", "CSV (delimited by pipe `|`)"),
                    (114, "Stata v10 or later"),
                    (117, "Stata v13 or later"),
                    (118, "Stata v14 or later"),
                    (119, "Stata v15 or later"),
                ],
                default="CSV",
                max_length=25,
            ),
        ),
        migrations.AlterField(
            model_name="historicaldatarequest",
            name="export_format",
            field=models.CharField(
                choices=[
                    ("CSV", "CSV (delimited by pipe `|`)"),
                    (114, "Stata v10 or later"),
                    (117, "Stata v13 or later"),
                    (118, "Stata v14 or later"),
                    (119, "Stata v15 or later"),
                ],
                default="CSV",
                max_length=25,
            ),
        ),
    ]
