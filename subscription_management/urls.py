from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from manage_subscription.rest.views.subscription import subscription_list_view

schema_view = get_schema_view(
    openapi.Info(
        title="Subscription Management",
        default_version="main",
        license=openapi.License(name="BSD License"),
    ),
    public=False,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("admin", admin.site.urls),
    re_path(
        r"^docs/swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=10),
        name="schema-json",
    ),
    re_path(
        r"^docs/swagger$",
        schema_view.with_ui("swagger", cache_timeout=10),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^docs/redoc$",
        schema_view.with_ui("redoc", cache_timeout=10),
        name="schema-redoc",
    ),
    # JWT Token
    path(
        "api/token",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "api/token/refresh",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path(
        "api/token/verify",
        TokenVerifyView.as_view(),
        name="token_verify",
    ),
    path("api/", include("manage_subscription.rest.urls.subscription")),
    path("api/auth/", include("core.rest.urls.registration")),
    path("api/exchange-rate/", include("manage_subscription.rest.urls.exchange_rate")),
    path("", subscription_list_view, name="subscription-list-ui"),
]
