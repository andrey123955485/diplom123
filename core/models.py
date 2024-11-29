from django.db import models

class Item(models.Model):
    CATEGORY_CHOICES = [
        ('Продукты питания', 'Продукты питания'),
        ('Стекло', 'Стекло'),
        ('Электроника', 'Электроника'),
        ('Мебель', 'Мебель'),
    ]

    TYPE_CHOICES = [
        ('Легкий', 'Легкий'),
        ('Тяжелый', 'Тяжелый'),
        ('Хрупкий', 'Хрупкий'),
        ('Опасный', 'Опасный'),
    ]

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    weight = models.FloatField()
    quantity = models.PositiveIntegerField()
    added_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='item_images/', null=True, blank=True)  # Добавлено поле для изображения

    def __str__(self):
        return self.name
