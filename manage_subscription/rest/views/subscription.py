from rest_framework import generics

from manage_subscription.models import Subscription
from manage_subscription.rest.serializers.subscription import (
    SubscriptionCancelSerializer,
    SubscriptionSerializer,
)


class SubscriptionCreateView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Subscription.objects.filter(user_id=user.id)
        return queryset


class SubscriptionListView(generics.ListAPIView):
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Subscription.objects.filter(user_id=user.id)
        return queryset


class SubscriptionCancelView(generics.UpdateAPIView):
    serializer_class = SubscriptionCancelSerializer
    lookup_field = "id"

    def get_queryset(self):
        user = self.request.user
        queryset = Subscription.objects.filter(user_id=user.id)
        return queryset
