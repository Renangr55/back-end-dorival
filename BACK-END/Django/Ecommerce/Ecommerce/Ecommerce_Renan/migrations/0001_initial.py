# Generated by Django 5.1.6 on 2025-02-14 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tituloProduto', models.CharField(max_length=200)),
                ('preco', models.FloatField()),
                ('descricaoProduto', models.TextField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
