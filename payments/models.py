from django.db import models


class Item(models.Model):
    CURRENCY = (
        ('USD', 'USD'),
        ('RUB', 'RUB')
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=255
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    price = models.IntegerField(
        verbose_name='Цена'
    )
    currency = models.CharField(
        max_length=255,
        choices=CURRENCY,
        default='RUB',
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Order(models.Model):
    payer = models.CharField(
        verbose_name='Плательщик',
        max_length=255
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    items = models.ManyToManyField(
        Item,
        related_name='order'
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ от: {self.created_at.strftime("%Y-%m-%d")}'
