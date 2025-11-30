from django.db import models

class Pizza(models.Model):
    """A Pizza the user is building."""
    name = models.CharField(max_length=200)
    def __str__(self):
        """Return a string representation of the pizzas."""
        return self.name

class Topping(models.Model):
    """Toppings user is adding to pizza."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        """Return a string representation of the toppings."""
        return self.name