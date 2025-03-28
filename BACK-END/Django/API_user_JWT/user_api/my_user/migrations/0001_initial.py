# Generated by Django 5.1.7 on 2025-03-28 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('idade', models.PositiveIntegerField()),
                ('telephone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=200)),
                ('education', models.CharField(max_length=10)),
                ('numbersAnimals', models.CharField(max_length=10)),
            ],
        ),
    ]
