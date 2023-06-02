from rest_framework import generics
from generalsettings.models import GeneralSettings
from .serializers import GeneralSettingsSerializer

class GeneralSettingsListAPIView(generics.ListAPIView):
    queryset = GeneralSettings.objects.all()
    serializer_class = GeneralSettingsSerializer

class GeneralSettingsCreateAPIView(generics.CreateAPIView):
    queryset = GeneralSettings.objects.all()
    serializer_class = GeneralSettingsSerializer

class GeneralSettingsRetrieveAPIView(generics.RetrieveAPIView):
    queryset = GeneralSettings.objects.all()
    serializer_class = GeneralSettingsSerializer

class GeneralSettingsUpdateAPIView(generics.UpdateAPIView):
    queryset = GeneralSettings.objects.all()
    serializer_class = GeneralSettingsSerializer

class GeneralSettingsDestroyAPIView(generics.DestroyAPIView):
    queryset = GeneralSettings.objects.all()
    serializer_class = GeneralSettingsSerializer
