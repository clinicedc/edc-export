# Generated by Django 4.2.3 on 2023-07-18 17:27

import django.db.models.deletion
import edc_sites.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sites", "0002_alter_domain_unique"),
        ("edc_export", "0014_alter_plan_options"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="datarequest",
            managers=[
                ("on_site", edc_sites.models.CurrentSiteManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name="datarequesthistory",
            managers=[
                ("on_site", edc_sites.models.CurrentSiteManager()),
            ],
        ),
        migrations.AddField(
            model_name="datarequest",
            name="site",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="sites.site",
            ),
        ),
        migrations.AddField(
            model_name="datarequesthistory",
            name="site",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="sites.site",
            ),
        ),
        migrations.AddField(
            model_name="historicaldatarequest",
            name="site",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="sites.site",
            ),
        ),
    ]
