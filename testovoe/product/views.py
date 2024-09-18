from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_xml.renderers import XMLRenderer
from rest_framework.response import Response


from .models import Product
from .serializers import ProductSerializer


class ProductTariffPromotionView(APIView):
    renderer_classes = [XMLRenderer]
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
