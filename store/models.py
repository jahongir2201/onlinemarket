from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField()

    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    type = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.TextField()
    UZ='Sum'
    RU='Rub'
    US='$'
    type_money=(
        (UZ,'Sum'),
        (RU, 'Rub'),
        (US, '$'),
    )
    price_type = models.CharField(max_length=10,
                                  choices=type_money,
                                  default='Sum')
    price = models.PositiveIntegerField()
    image = models.ImageField()

    def __str__(self):
        return self.name