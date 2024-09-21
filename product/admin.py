from django.contrib import admin

from common.models import Media
from .models import Category, Product, ProductImage, ProductSize, ProductColor, ProductReview, WishList



admin.site.register(Category)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductColorInline(admin.TabularInline):
    model = ProductColor
    extra = 1

class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'quantity', 'category', 'in_stock']
    inlines = [ProductImageInline, ProductColorInline, ProductSizeInline]

admin.site.register(ProductImage)
admin.site.register(ProductSize)
admin.site.register(ProductColor)
admin.site.register(ProductReview)
admin.site.register(WishList)
