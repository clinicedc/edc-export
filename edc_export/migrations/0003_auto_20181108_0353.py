# Generated by Django 2.1.2 on 2018-11-08 01:53

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("edc_export", "0002_auto_20180922_1843")]

    operations = [
        migrations.AlterField(
            model_name="historicaldatarequest",
            name="history_id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="historicalexportreceipt",
            name="history_id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="historicalfilehistory",
            name="history_id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="historicalobjecthistory",
            name="history_id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="historicalplan",
            name="history_id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
