from rest_framework import serializers

from .models import *

from datetime import datetime
import decimal


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ('promotion_name', 'discount_percent', 'end_date')


class TariffSerializer(serializers.ModelSerializer):
    best_promotion = serializers.SerializerMethodField()
    discounted_price = serializers.SerializerMethodField()

    class Meta:
        model = Tariff
        fields = ('tariff_name', 'base_price', 'best_promotion', 'discounted_price')

    def get_best_promotion(self, obj):
        current_date = datetime.now().date()
        current_promotions = obj.promotions.filter(start_date__lte=current_date, end_date__gte=current_date).all()
        promotion = current_promotions.order_by('-discount_percent').first()
        if promotion:
            return PromotionSerializer(promotion).data
        return None

    def get_discounted_price(self, obj):
        promotion = obj.promotions.order_by('-discount_percent').first()
        if promotion:
            return round(obj.base_price * decimal.Decimal(1 - promotion.discount_percent / 100), 2)
        return obj.base_price


class ProductSerializer(serializers.ModelSerializer):
    tariffs = TariffSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['product_name', 'tariffs']
