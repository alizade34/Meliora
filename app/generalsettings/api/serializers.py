from rest_framework import serializers
from generalsettings.models import GeneralSettings

class GeneralSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralSettings
        fields = '__all__'