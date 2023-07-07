# Generated by Django 4.2 on 2023-04-12 23:27

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("model", models.CharField(max_length=200)),
                ("brand", models.CharField(max_length=200)),
                ("factory_year", models.IntegerField(blank=True, null=True)),
                ("model_year", models.IntegerField(blank=True, null=True)),
                ("value", models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
