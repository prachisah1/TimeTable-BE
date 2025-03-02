# Generated by Django 5.1.3 on 2025-02-11 17:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0009_alter_teacher_password"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="teacher",
            name="email",
        ),
        migrations.RemoveField(
            model_name="teacher",
            name="name",
        ),
        migrations.RemoveField(
            model_name="teacher",
            name="password",
        ),
        migrations.AddField(
            model_name="teacher",
            name="user",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
