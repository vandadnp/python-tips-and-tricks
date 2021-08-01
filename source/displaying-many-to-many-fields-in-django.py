# Want to support my work 🤝? https://buymeacoffee.com/vandad

from django.db import models


class Topping(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    def __str__(self) -> str:
        return f"{self.name}"


class Pizza(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="The name of the pizza, such as Pepperoni",
    )
    toppings = models.ManyToManyField(
        Topping,
        verbose_name="Toppings of a pizza",
    )

    def get_toppings(self) -> str:
        return ", ".join([t.name for t in self.toppings.all()])

    def __str__(self) -> str:
        return f"{self.name}, toppings = {self.get_toppings()}"
