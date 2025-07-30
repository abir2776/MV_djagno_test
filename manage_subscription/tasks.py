import requests
from celery import shared_task
from django.conf import settings

from .models import ExchangeRateLog


@shared_task
def fetch_exchange_rate():
    """Fetches USD to BDT exchange rate every hour"""
    api_key = settings.EXCHANGE_RATE_API_KEY
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/USD/BDT"

    response = requests.get(url)
    data = response.json()
    rate = data.get("conversion_rate")
    ExchangeRateLog.objects.create(
        base_currency="USD", target_currency="BDT", rate=rate
    )
