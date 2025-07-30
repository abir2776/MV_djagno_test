import requests
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ...models import ExchangeRateLog


class ExchangeRateView(APIView):
    def get(self, request):
        base = request.query_params.get("base", "USD")
        target = request.query_params.get("target", "BDT")

        api_key = settings.EXCHANGE_RATE_API_KEY
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base}/{target}"

        response = requests.get(url)

        if response.status_code != 200:
            return Response(
                {"error": "Failed to fetch exchange rate"},
                status=status.HTTP_502_BAD_GATEWAY,
            )

        data = response.json()

        if data.get("result") != "success":
            return Response(
                {"error": data.get("error-type", "Unknown error")},
                status=status.HTTP_400_BAD_REQUEST,
            )

        rate = data.get("conversion_rate")

        ExchangeRateLog.objects.create(
            base_currency=base, target_currency=target, rate=rate
        )

        return Response(
            {"base": base, "target": target, "rate": rate}, status=status.HTTP_200_OK
        )
