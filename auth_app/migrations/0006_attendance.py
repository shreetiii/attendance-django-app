# Generated by Django 5.1 on 2024-09-22 11:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auth_app", "0005_studentclass"),
    ]

    operations = [
        migrations.CreateModel(
            name="Attendance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("today_date", models.DateField()),
                (
                    "stats",
                    models.CharField(
                        choices=[("P", "Present"), ("A", "Absent")], max_length=1
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="auth_app.course",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="auth_app.student",
                    ),
                ),
            ],
            options={
                "db_table": "attendance",
            },
        ),
    ]
