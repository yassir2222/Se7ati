# Generated by Django 5.1.7 on 2025-03-27 00:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("se7ati_app", "0009_mesureglycemie"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mesureglycemie",
            name="date_mesure",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
