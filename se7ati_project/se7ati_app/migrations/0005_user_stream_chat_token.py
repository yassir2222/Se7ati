# Generated by Django 5.0.4 on 2025-03-22 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('se7ati_app', '0004_quartier'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='stream_chat_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
