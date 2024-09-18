from django.db import models

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Название продукта')

    class Meta:
        verbose_name = 'продут'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return self.product_name


class Tariff(models.Model):
    tariff_name = models.CharField(max_length=255)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='tariffs')

    class Meta:
        verbose_name = 'тариф'
        verbose_name_plural = 'тарифы'

    def __str__(self):
        return self.tariff_name


class Promotion(models.Model):
    promotion_name = models.CharField(max_length=255)
    discount_percent = models.PositiveIntegerField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    tariffs = models.ManyToManyField('Tariff', verbose_name='Тариф', related_name='promotions')

    class Meta:
        verbose_name = 'продвижение'
        verbose_name_plural = 'продвижения'

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError('Конец продвижения должен быть позже начала!')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.promotion_name
