# Generated by Django 5.1.3 on 2025-02-13 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0012_subject_is_special_subject_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="teachersubject",
            name="subject_id",
        ),
        migrations.RemoveField(
            model_name="teachersubject",
            name="teacher_id",
        ),
        migrations.AddField(
            model_name="teachersubject",
            name="subject_teacher_map",
            field=models.JSONField(default=dict),
        ),
    ]
