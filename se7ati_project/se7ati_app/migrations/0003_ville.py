# Generated by Django 5.1.7 on 2025-03-22 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("se7ati_app", "0002_remove_user_is_patient_user_user_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ville",
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
                (
                    "nom",
                    models.CharField(max_length=100, verbose_name="Nom de la ville"),
                ),
            ],
        ),
    ]
