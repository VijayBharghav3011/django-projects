# Generated by Django 5.0.3 on 2024-11-05 07:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todo_list", "0004_alter_tasklist_assigned_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tasklist",
            name="title",
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
