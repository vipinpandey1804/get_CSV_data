from django.db import models
# Create your models here.

class AxisValue(models.Model):
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    open = models.DecimalField(max_digits=10, decimal_places=3)
    high = models.DecimalField(max_digits=10, decimal_places=3)
    low = models.DecimalField(max_digits=10, decimal_places=3)
    vol = models.CharField(max_length=20)

    class Meta:
        abstract = True


class GoldAssetGraphData(AxisValue):
    def __str__(self) -> str:
        return str(self.date)    


class SilverAssetGraphData(AxisValue):
    def __str__(self) -> str:
        return str(self.date)


class CopperAssetGraphData(AxisValue):
    def __str__(self) -> str:
        return str(self.date)


class PlatinumAssetGraphData(AxisValue):
    def __str__(self) -> str:
        return str(self.date)


class OilAssetGraphData(AxisValue):
    def __str__(self) -> str:
        return str(self.date)


class NaturalGasAssetGraphData(AxisValue):
    def __str__(self) -> str:
        return str(self.date)
