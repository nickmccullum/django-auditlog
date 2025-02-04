# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

# from jsonfield_compat import JSONField


class Migration(migrations.Migration):

    dependencies = [
        ("auditlog", "0003_logentry_remote_addr"),
    ]

    operations = [
        migrations.AddField(
            model_name="logentry",
            name="additional_data",
            field=models.JSONField(null=True, blank=True),
        ),
    ]
