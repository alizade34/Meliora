from django.urls import path
from .views import (
    GeneralSettingsListAPIView,
    GeneralSettingsCreateAPIView,
    GeneralSettingsRetrieveAPIView,
    GeneralSettingsUpdateAPIView,
    GeneralSettingsDestroyAPIView,
)
app_name = "generalsettings-api"
urlpatterns = [
    path('list/', GeneralSettingsListAPIView.as_view(), name='list'),
    path('create/', GeneralSettingsCreateAPIView.as_view(), name='create'),
    path('update/', GeneralSettingsUpdateAPIView.as_view(), name='update'),
    path('delete/', GeneralSettingsDestroyAPIView.as_view(), name='delete'),
]
