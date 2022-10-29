from rest_framework.serializers import ModelSerializer
from .models import *

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductSerializer(ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = "__all__"

class CustomerSerializer():
    class Meta:
        model = Customer
        fields = "__all__"


class OrderSerializer(ModelSerializer):
    customer = CustomerSerializer()
    class Meta:
        model = Order
        fields = "__all__"