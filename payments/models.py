from django.db import models


class Item(models.Model):
    """Describdes one item of a product."""

    name = models.CharField(
        verbose_name="Единица товара",
        max_length=255,
        unique=True,
        blank=False,
        null=False,
    )
    description = models.TextField(
        verbose_name="Описание товара",
        blank=False,
        null=False,
    )
    price = models.DecimalField(
        verbose_name="Цена товара",
        max_digits=10,
        decimal_places=2,
        blank=False,
        null=False,
    )

    def __str__(self) -> str:
        return self.name
