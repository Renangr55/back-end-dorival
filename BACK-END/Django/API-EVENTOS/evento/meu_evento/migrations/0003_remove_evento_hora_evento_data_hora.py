# Generated by Django 5.1.7 on 2025-03-14 18:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meu_evento', '0002_rename_eventos_evento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='hora',
        ),
        migrations.AddField(
            model_name='evento',
            name='data_hora',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
