# Generated by Django 5.1 on 2024-09-17 13:57

import auth_app.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auth_app", "0002_alter_teacher_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("name", models.CharField(max_length=30)),
                ("address", models.CharField(max_length=30)),
                (
                    "age",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(20),
                            django.core.validators.MaxValueValidator(30),
                        ]
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        max_length=10,
                        unique=True,
                        validators=[django.core.validators.MinLengthValidator(10)],
                    ),
                ),
            ],
            options={
                "verbose_name": "Student",
                "db_table": "student",
                "ordering": ["name"],
            },
        ),
        migrations.AlterField(
            model_name="teacher",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to=auth_app.models.file_upload
            ),
        ),
    ]
