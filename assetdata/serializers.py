from rest_framework import serializers
from .models import GoldAssetGraphData, SilverAssetGraphData, CopperAssetGraphData, PlatinumAssetGraphData, OilAssetGraphData, NaturalGasAssetGraphData

class GoldAssetGraphDataSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateField(source='date')
    class Meta:
        model = GoldAssetGraphData  # Choose any model, as the fields are the same for all models
        exclude = ("id",)
    
class SilverAssetGraphDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SilverAssetGraphData  # Choose any model, as the fields are the same for all models
        exclude = ("id",)

class CopperAssetGraphDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CopperAssetGraphData  # Choose any model, as the fields are the same for all models
        exclude = ("id",)

class PlatinumAssetGraphDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatinumAssetGraphData  # Choose any model, as the fields are the same for all models
        exclude = ("id",)

class OilAssetGraphDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = OilAssetGraphData  # Choose any model, as the fields are the same for all models
        exclude = ("id",)

class NaturalGasAssetGraphDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = NaturalGasAssetGraphData  # Choose any model, as the fields are the same for all models
        exclude = ("id",)