# Generated by Django 2.1.5 on 2019-01-12 19:50

from __future__ import annotations

from typing import Any

from django.apps.registry import Apps
from django.db import migrations


def set_badge_key(apps: Apps, schema_editor: Any) -> None:
    Project = apps.get_model("accounts", "Project")
    for project in Project.objects.select_related("owner").all():
        project.badge_key = project.owner.username
        project.save()


class Migration(migrations.Migration):
    dependencies = [("accounts", "0019_project_badge_key")]

    operations = [migrations.RunPython(set_badge_key, migrations.RunPython.noop)]
