# Generated by Django 5.1.7 on 2025-04-13 20:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('se7ati_app', '0011_article'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='publication_date',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='article',
            name='user',
        ),
        migrations.AlterField(
            model_name='article',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
