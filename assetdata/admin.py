from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(GoldAssetGraphData)
admin.site.register(SilverAssetGraphData)
admin.site.register(PlatinumAssetGraphData)
admin.site.register(CopperAssetGraphData)
admin.site.register(OilAssetGraphData)
admin.site.register(NaturalGasAssetGraphData)