from django.db import models

from account.models import User, UserAddress
from common.models import Region
from product.models import Product


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    subtotal = models.FloatField()

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        self.subtotal = self.quantity * self.product.price

        super(CartItem, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Cart item'
        verbose_name_plural = 'Cart items'


class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_name = models.CharField(max_length=120)
    card_number = models.CharField(max_length=60)
    expire_date = models.DateTimeField()
    cvv = models.CharField(max_length=3)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'


class Discount(models.Model):
    code = models.CharField(max_length=60)
    max_limit_price = models.FloatField()
    percertage = models.FloatField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Discount'
        verbose_name_plural = 'Discounts'


class Branch(models.Model):
    name = models.CharField(max_length=120)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=10)
    street = models.CharField(max_length=120)
    address = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Branch'
        verbose_name_plural = 'Branchs'


class DeliveryTariff(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    high = models.FloatField()
    width =models.FloatField()
    weight = models.FloatField()
    price = models.FloatField()
    regions = models.ManyToManyField(Region, related_name='delivery_tariff')
    delivary_time = models.TimeField()

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Delivery tariff'
        verbose_name_plural = 'Delivery tariff'


class Order(models.Model):
    class OrderStatus(models.TextChoices):
        CREATED = 'created', 'Created'
        IN_PROGRESS = 'in_progress', 'In_progress'
        DELIVERED = 'delivered', 'Delivered'
        CANCELLED = 'cancelled', 'Cancelled'
        FINISHED = 'finished', 'Finished'

    class PaymentStatus(models.TextChoices):
        CREATED = 'created', 'Created'
        PENDING = 'pending', 'Pending'
        PAID = 'paid', 'Paid'
        CANCELLED = 'cancelled', 'Cancelled'

    class PaymentMethod(models.TextChoices):
        CASH = 'cash', 'Cash'
        PAYME = 'payme', 'Payme'
        CLICK = 'click', 'Click'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=60, choices=OrderStatus.choices)
    items = models.ManyToManyField(CartItem, related_name='orders')
    total_price = models.FloatField()
    address = models.ForeignKey(UserAddress, on_delete=models.CASCADE, related_name='orders')
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)
    payment_status = models.CharField(max_length=60, choices=PaymentStatus.choices)
    payment_method = models.CharField(max_length=60, choices=PaymentMethod.choices)
    delivery_tariff = models.ForeignKey(DeliveryTariff, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


