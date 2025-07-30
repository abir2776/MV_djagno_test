from django.db import models

from common.models import BaseModelWithUID

from .choices import SubscriptionStatus


class Plan(BaseModelWithUID):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    duration_days = models.PositiveIntegerField()

    def __str__(self):
        return f"Name: {self.name}, Duration: {self.duration_days}"


class Subscription(BaseModelWithUID):
    user = models.ForeignKey("core.User", on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=SubscriptionStatus.choices,
        default=SubscriptionStatus.ACTIVE,
    )

    class Meta:
        unique_together = ("user", "plan")

    def __str__(self):
        return f"User: {self.user.id}, Plan: {self.plan.id}, Status: {self.status}"


class ExchangeRateLog(BaseModelWithUID):
    base_currency = models.CharField(default="USD")
    target_currency = models.CharField(default="BDT")
    rate = models.PositiveIntegerField()
    fetched_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("base_currency", "target_currency")

    def __str__(self):
        return f"Base Currency: {self.base_currency}, Target Currency: {self.target_currency}, Fetched_at: {self.fetched_at}"
