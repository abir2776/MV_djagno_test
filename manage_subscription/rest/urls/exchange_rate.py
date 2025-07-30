from django.urls import path

from ..views.exchange_rate import ExchangeRateView

urlpatterns = [
    path("", ExchangeRateView.as_view(), name="exchange-rate"),
]
