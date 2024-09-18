from django.contrib import admin
from .models import Product, Tariff, Promotion


class TariffInline(admin.TabularInline):
    model = Tariff
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name',)

    inlines = [TariffInline]


@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = ('tariff_name', 'base_price', 'product')
    list_filter = ('product',)


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('promotion_name', 'discount_percent', 'start_date', 'end_date')
