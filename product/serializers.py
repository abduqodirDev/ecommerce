from rest_framework import serializers

from common.serializers import MediaSerializer
from .models import Category, Product


class CategoryListSerializer(serializers.ModelSerializer):
    parent = serializers.SerializerMethodField("just")
    class Meta:
        model = Category
        fields = ("name","parent")

    def just(self, obj):
        if obj.parent:
            just = obj.parent
            return just.name
        else:
            return None

    # def to_representation(self, instance):
    #     data = super(CategoryListSerializer, self).to_representation(instance)
    #     if data['parent']:
    #         id = data['parent']
    #         data['parent'] = Category.objects.get(id=id).name
    #     return data


class ProductListSerializer(serializers.ModelSerializer):
    thumbnail = MediaSerializer(read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'category', 'in_stock', 'brand', 'discount', 'thumbnail')


class ProductColorSerializer(serializers.Serializer):
    image = MediaSerializer(read_only=True)
    id = serializers.IntegerField()


class ProductSizeSerializer(serializers.Serializer):
    value = serializers.CharField()
    id = serializers.IntegerField()
