# Generated by Django 5.1.7 on 2025-04-06 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("con_app", "0007_alter_environmentalcondition_precations"),
    ]

    operations = [
        migrations.AddField(
            model_name="seller",
            name="details",
            field=models.TextField(
                blank=True, default="No details Provided", null=True
            ),
        ),
    ]
