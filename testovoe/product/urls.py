from django.urls import path
from .views import ProductTariffPromotionView


urlpatterns = [
    path(r'product/', ProductTariffPromotionView.as_view()),
]