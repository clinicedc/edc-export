# Generated by Django 2.1.7 on 2019-03-04 23:23

import django_audit_fields.fields.hostname_modification_field
import django_audit_fields.fields.userfield
import django_audit_fields.models.audit_model_mixin
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("edc_export", "0003_auto_20181108_0353")]

    operations = [
        migrations.AlterField(
            model_name="datarequest",
            name="created",
            field=models.DateTimeField(
                blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
            ),
        ),
        migrations.AlterField(
            model_name="datarequest",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="datarequest",
            name="modified",
            field=models.DateTimeField(
                blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
            ),
        ),
        migrations.AlterField(
            model_name="datarequest",
            name="user_created",
            field=django_audit_fields.fields.userfield.UserField(
                blank=True,
                help_text="Updated by admin.save_model",
                max_length=50,
                verbose_name="user created",
            ),
        ),
        migrations.AlterField(
            model_name="datarequest",
            name="user_modified",
            field=django_audit_fields.fields.userfield.UserField(
                blank=True,
                help_text="Updated by admin.save_model",
                max_length=50,
                verbose_name="user modified",
            ),
        ),
        migrations.AlterField(
            model_name="datarequesthistory",
            name="created",
            field=models.DateTimeField(
                blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
            ),
        ),
        migrations.AlterField(
            model_name="datarequesthistory",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="datarequesthistory",
            name="modified",
            field=models.DateTimeField(
                blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
            ),
        ),
        migrations.AlterField(
            model_name="datarequesthistory",
            name="user_created",
            field=django_audit_fields.fields.userfield.UserField(
                blank=True,
                help_text="Updated by admin.save_model",
                max_length=50,
                verbose_name="user created",
            ),
        ),
        migrations.AlterField(
            model_name="datarequesthistory",
            name="user_modified",
            field=django_audit_fields.fields.userfield.UserField(
                blank=True,
                help_text="Updated by admin.save_model",
                max_length=50,
                verbose_name="user modified",
            ),
        ),
        migrations.AlterField(
            model_name="exportreceipt",
            name="created",
            field=models.DateTimeField(
                blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
            ),
        ),
        migrations.AlterField(
            model_name="exportreceipt",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="exportreceipt",
            name="modified",
            field=models.DateTimeField(
                blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
            ),
        ),
        migrations.AlterField(
            model_name="exportreceipt",
            name="user_created",
            field=django_audit_fields.fields.userfield.UserField(
                blank=True,
                help_text="Updated by admin.save_model",
                max_length=50,
                verbose_name="user created",
            ),
        ),
        migrations.AlterField(
            model_name="exportreceipt",
            name="user_modified",
            field=django_audit_fields.fields.userfield.UserField(
                blank=True,
                help_text="Updated by admin.save_model",
                max_length=50,
                verbose_name="user modified",
            ),
        ),
        migrations.AlterField(
            model_name="filehistory",
            name="created",
            field=models.DateTimeField(
                blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
            ),
        ),
        migrations.AlterField(
            model_name="filehistory",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="filehistory",
            name="modified",
            field=models.DateTimeField(
                blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
            ),
        ),
        migrations.AlterField(
            model_name="filehistory",
            name="user_created",
            field=django_audit_fields.fields.userfield.UserField(
                blank=True,
                help_text="Updated by admin.save_model",
                max_length=50,
                verbose_name="user created",
            ),
        ),
        migrations.AlterField(
            model_name="filehistory",
            name="user_modified",
            field=django_audit_fields.fields.userfield.UserField(
                blank=True,
                help_text="Updated by admin.save_model",
                max_length=50,
                verbose_name="user modified",
            ),
        ),
        migrations.AlterField(
            model_name="historicaldatarequest",
            name="created",
            field=models.DateTimeField(
                blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
            ),
        ),
        migrations.AlterField(
            model_name="historicaldatarequest",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="historicaldatarequest",
            name="modified",
            field=models.DateTimeField(
                blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
            ),
        ),
        migrations.AlterField(
            model_name="historicaldatarequest",
            name="user_created",
            field=django_audit_fields.fields.userfield.UserField(
                blank=True,
                help_text="Updated by admin.save_model",
                max_length=50,
                verbose_name="user created",
            ),
        ),
        migrations.AlterField(
            model_name="historicaldatarequest",
            name="user_modified",
            field=django_audit_fields.fields.userfield.UserField(
                blank=True,
                help_text="Updated by admin.save_model",
                max_length=50,
                verbose_name="user modified",
            ),
        ),
        migrations.AlterField(
            model_name="historicalexportreceipt",
            name="created",
            field=models.DateTimeField(
                blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
            ),
        ),
        migrations.AlterField(
            model_name="historicalexportreceipt",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="historicalexportreceipt",
            name="modified",
            field=models.DateTimeField(
                blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
            ),
        ),
        migrations.AlterField(
            model_name="historicalexportreceipt",
            name="user_created",
            field=django_audit_fields.fields.userfield.UserField(
                blank=True,
                help_text="Updated by admin.save_model",
                max_length=50,
                verbose_name="user created",
            ),
        ),
        migrations.AlterField(
            model_name="historicalexportreceipt",
            name="user_modified",
            field=django_audit_fields.fields.userfield.UserField(
                blank=True,
                help_text="Updated by admin.save_model",
                max_length=50,
                verbose_name="user modified",
            ),
        ),
        migrations.AlterField(
            model_name="historicalfilehistory",
            name="created",
            field=models.DateTimeField(
                blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
            ),
        ),
        migrations.AlterField(
            model_name="historicalfilehistory",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="historicalfilehistory",
            name="modified",
            field=models.DateTimeField(
                blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
            ),
        ),
        migrations.AlterField(
            model_name="historicalfilehistory",
            name="user_created",
            field=django_audit_fields.fields.userfield.UserField(
                blank=True,
                help_text="Updated by admin.save_model",
                max_length=50,
                verbose_name="user created",
            ),
        ),
        migrations.AlterField(
            model_name="historicalfilehistory",
            name="user_modified",
            field=django_audit_fields.fields.userfield.UserField(
                blank=True,
                help_text="Updated by admin.save_model",
                max_length=50,
                verbose_name="user modified",
            ),
        ),
        migrations.AlterField(
            model_name="historicalobjecthistory",
            name="created",
            field=models.DateTimeField(
                blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
            ),
        ),
        migrations.AlterField(
            model_name="historicalobjecthistory",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="historicalobjecthistory",
            name="modified",
            field=models.DateTimeField(
                blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
            ),
        ),
        migrations.AlterField(
            model_name="historicalobjecthistory",
            name="user_created",
            field=django_audit_fields.fields.userfield.UserField(
                blank=True,
                help_text="Updated by admin.save_model",
                max_length=50,
                verbose_name="user created",
            ),
        ),
        migrations.AlterField(
            model_name="historicalobjecthistory",
            name="user_modified",
            field=django_audit_fields.fields.userfield.UserField(
                blank=True,
                help_text="Updated by admin.save_model",
                max_length=50,
                verbose_name="user modified",
            ),
        ),
        migrations.AlterField(
            model_name="historicalplan",
            name="created",
            field=models.DateTimeField(
                blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
            ),
        ),
        migrations.AlterField(
            model_name="historicalplan",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="historicalplan",
            name="modified",
            field=models.DateTimeField(
                blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
            ),
        ),
        migrations.AlterField(
            model_name="historicalplan",
            name="user_created",
            field=django_audit_fields.fields.userfield.UserField(
                blank=True,
                help_text="Updated by admin.save_model",
                max_length=50,
                verbose_name="user created",
            ),
        ),
        migrations.AlterField(
            model_name="historicalplan",
            name="user_modified",
            field=django_audit_fields.fields.userfield.UserField(
                blank=True,
                help_text="Updated by admin.save_model",
                max_length=50,
                verbose_name="user modified",
            ),
        ),
        migrations.AlterField(
            model_name="objecthistory",
            name="created",
            field=models.DateTimeField(
                blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
            ),
        ),
        migrations.AlterField(
            model_name="objecthistory",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="objecthistory",
            name="modified",
            field=models.DateTimeField(
                blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
            ),
        ),
        migrations.AlterField(
            model_name="objecthistory",
            name="user_created",
            field=django_audit_fields.fields.userfield.UserField(
                blank=True,
                help_text="Updated by admin.save_model",
                max_length=50,
                verbose_name="user created",
            ),
        ),
        migrations.AlterField(
            model_name="objecthistory",
            name="user_modified",
            field=django_audit_fields.fields.userfield.UserField(
                blank=True,
                help_text="Updated by admin.save_model",
                max_length=50,
                verbose_name="user modified",
            ),
        ),
        migrations.AlterField(
            model_name="plan",
            name="created",
            field=models.DateTimeField(
                blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
            ),
        ),
        migrations.AlterField(
            model_name="plan",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="plan",
            name="modified",
            field=models.DateTimeField(
                blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
            ),
        ),
        migrations.AlterField(
            model_name="plan",
            name="user_created",
            field=django_audit_fields.fields.userfield.UserField(
                blank=True,
                help_text="Updated by admin.save_model",
                max_length=50,
                verbose_name="user created",
            ),
        ),
        migrations.AlterField(
            model_name="plan",
            name="user_modified",
            field=django_audit_fields.fields.userfield.UserField(
                blank=True,
                help_text="Updated by admin.save_model",
                max_length=50,
                verbose_name="user modified",
            ),
        ),
        migrations.AlterField(
            model_name="uploadexportreceiptfile",
            name="created",
            field=models.DateTimeField(
                blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
            ),
        ),
        migrations.AlterField(
            model_name="uploadexportreceiptfile",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="uploadexportreceiptfile",
            name="modified",
            field=models.DateTimeField(
                blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
            ),
        ),
        migrations.AlterField(
            model_name="uploadexportreceiptfile",
            name="user_created",
            field=django_audit_fields.fields.userfield.UserField(
                blank=True,
                help_text="Updated by admin.save_model",
                max_length=50,
                verbose_name="user created",
            ),
        ),
        migrations.AlterField(
            model_name="uploadexportreceiptfile",
            name="user_modified",
            field=django_audit_fields.fields.userfield.UserField(
                blank=True,
                help_text="Updated by admin.save_model",
                max_length=50,
                verbose_name="user modified",
            ),
        ),
    ]
