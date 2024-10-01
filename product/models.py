from ckeditor.fields import RichTextField

from django.db import models

from account.models import User
from common.models import Media


class Category(models.Model):
    name = models.CharField(max_length=120)
    image = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.FloatField()
    short_description = models.TextField()
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    instructions = RichTextField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    in_stock = models.BooleanField(default=True)
    brand = models.CharField(max_length=120)
    discount = models.PositiveIntegerField()
    thumbnail = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductImage(models.Model):
    image = models.ForeignKey(Media, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Product image'
        verbose_name_plural = 'Product images'


class ProductColor(models.Model):
    image = models.ForeignKey(Media, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="colors")

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Product color'
        verbose_name_plural = 'Product colors'


class ProductSize(models.Model):
    value = models.CharField(max_length=30)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sizes")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Product size'
        verbose_name_plural = 'Product sizes'


class ProductReview(models.Model):
    user = models.ForeignKey('account.user', on_delete=models.CASCADE)
    rank = models.IntegerField()
    title = models.CharField(max_length=120)
    review = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=120)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Product review'
        verbose_name_plural = 'Product reviews'


class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Wish list'
        verbose_name_plural = 'Wish lists'