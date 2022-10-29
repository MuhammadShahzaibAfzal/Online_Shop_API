from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from core.serializers import ProductSerializer
from .models import Product,Category
# Create your views here.

def home(request):
    return HttpResponse("<h1>Welcome to shop API</h1>")


class ProductView(APIView):
    def get(self,request):
        products= Product.objects.all()
        serializer = ProductSerializer(products,many=True)

        return Response(serializer.data)

class SingleProductView(APIView):
    def get_product(self,pk):
        product = Product.objects.get(id=pk)
        return product

    def get(self,request,pk):
        product = self.get_product(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


