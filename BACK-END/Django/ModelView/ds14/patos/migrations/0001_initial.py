# Generated by Django 5.2 on 2025-04-10 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('especie', models.CharField(max_length=150)),
                ('idade', models.PositiveIntegerField()),
                ('peso', models.FloatField()),
                ('cor', models.CharField(max_length=50)),
                ('superPoder', models.CharField(max_length=200)),
                ('cagaTorrada', models.BooleanField(blank=True, null=True)),
            ],
        ),
    ]
