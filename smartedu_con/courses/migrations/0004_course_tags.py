# Generated by Django 5.0.3 on 2024-03-27 19:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0003_tag"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="tags",
            field=models.ManyToManyField(blank=True, null=True, to="courses.tag"),
        ),
    ]
