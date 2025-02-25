# Generated by Django 5.1.6 on 2025-02-25 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
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
                    "name",
                    models.CharField(
                        max_length=255,
                        unique=True,
                        verbose_name="Единица товара",
                    ),
                ),
                (
                    "description",
                    models.TextField(verbose_name="Описание товара"),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        verbose_name="Цена товара",
                    ),
                ),
            ],
        ),
    ]
