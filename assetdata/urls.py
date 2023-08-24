from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('gold', GoldAssetGraphDataViewSet,basename='gold')
router.register('silver', SilverAssetGraphDataViewSet,basename='silver')
router.register('copper', CopperAssetGraphDataViewSet,basename='copper')
router.register('platinum', PlatinumAssetGraphDataViewSet,basename='platinum')
router.register('oil', OilAssetGraphDataViewSet,basename='oil')
router.register('natural-gas', NaturalGasAssetGraphDataViewSet,basename='natural-gas')

urlpatterns = [
    path('save_data/', SaveAssetHistoricalCSVDataAPIView.as_view(), name='save-csv-data'),
    path('graph-data/',include(router.urls)),
]
