from django.db import models

CATEGORY_CHOICES = [
    ('for_him', 'For Him'),
    ('for_her', 'For Her'),
    ('dad', 'Dad'),
    ('mom', 'Mom'),
    ('graduation', 'Graduation'),
    ('friendship', 'Friendship'),
]

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    in_stock = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name