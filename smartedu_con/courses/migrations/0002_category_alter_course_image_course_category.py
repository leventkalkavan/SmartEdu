# Generated by Django 5.0.3 on 2024-03-27 18:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=50, null=True)),
                ("slug", models.SlugField(null=True, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name="course",
            name="image",
            field=models.ImageField(
                default="courses/defaultPic.jpg", upload_to="courses/%Y/%m/%d/"
            ),
        ),
        migrations.AddField(
            model_name="course",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="courses.category",
            ),
        ),
    ]
