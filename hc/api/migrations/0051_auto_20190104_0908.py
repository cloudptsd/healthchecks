# Generated by Django 2.1.4 on 2019-01-04 09:08

from __future__ import annotations

from typing import Any

from django.apps.registry import Apps
from django.db import migrations


def fill_ping_kind(apps: Apps, schema_editor: Any) -> None:
    Ping = apps.get_model("api", "Ping")

    q = Ping.objects.filter(start=True)
    q.update(kind="start")

    q = Ping.objects.filter(fail=True)
    q.update(kind="fail")


class Migration(migrations.Migration):
    dependencies = [("api", "0050_ping_kind")]

    operations = [migrations.RunPython(fill_ping_kind)]
