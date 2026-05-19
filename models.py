

class Food(models.Model):
    food_name = models.CharField(max_length=100)
    restaurant_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField()
    delivery_time = models.IntegerField()

    def __str__(self):
        return self.food_name