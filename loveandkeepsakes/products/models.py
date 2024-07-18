from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('for_him', 'For Him'),
        ('for_her', 'For Her'),
        ('dad', 'Dad'),
        ('mom', 'Mom'),
        ('graduation', 'Graduation'),
        ('friendship', 'Friendship'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.name
