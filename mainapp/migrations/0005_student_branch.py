# Generated by Django 5.1.3 on 2024-11-24 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0004_subject_branch"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="branch",
            field=models.CharField(default="", max_length=100),
        ),
    ]
