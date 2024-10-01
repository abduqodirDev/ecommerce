from django.shortcuts import render
from jsonschema.exceptions import ValidationError
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product
from .models import CartItem
from .serializers import AddToCartSerializer, UpdateCartItemSerializer


class AddToCartView(APIView):
    serializer_class = AddToCartSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            product = Product.objects.get(id=data.get('product_id'))
            item = CartItem.objects.create(user=request.user, product=product, quantity=data.get('quantity'))
            data = {
                'status': True,
                'message': 'cart item added'
            }
            return Response(data)

        except Product.DoesNotExist:
            data = {
                'status': False,
                'message': "product does not exist"
            }
            raise ValidationError(data)

        except Exception as e:
            raise e


class UpdateCartItemView(UpdateAPIView):
    serializer_class = UpdateCartItemSerializer
    queryset = CartItem.objects.all()
    permission_classes = [IsAuthenticated]

