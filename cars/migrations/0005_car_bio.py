# Generated by Django 4.2 on 2023-05-25 01:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cars", "0004_carinventory"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="bio",
            field=models.TextField(blank=True, null=True),
        ),
    ]
