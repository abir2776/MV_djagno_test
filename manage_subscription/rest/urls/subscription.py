from django.urls import path

from ..views.subscription import (
    SubscriptionCancelView,
    SubscriptionCreateView,
    SubscriptionListView,
)

urlpatterns = [
    path("subscriptions/", SubscriptionListView.as_view(), name="subscription-list"),
    path("subscription/", SubscriptionCreateView.as_view(), name="subscription-create"),
    path(
        "subscriptions/<int:id>/",
        SubscriptionCancelView.as_view(),
        name="subscription-cancel",
    ),
]
