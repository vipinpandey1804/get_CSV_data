import pandas as pd
import numpy as np
from datetime import datetime
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import AxisValue, GoldAssetGraphData, SilverAssetGraphData, CopperAssetGraphData, PlatinumAssetGraphData, OilAssetGraphData, NaturalGasAssetGraphData
from .serializers import *

class SaveAssetHistoricalCSVDataAPIView(APIView):
    def post(self, request, format=None):
        file_mapping = {
            "graph data/Brent Oil Futures Historical Data.csv": OilAssetGraphData,
            "graph data/Copper Futures Historical Data.csv": CopperAssetGraphData,
            "graph data/Gold Futures Historical Data.csv": GoldAssetGraphData,
            "graph data/Natural Gas Futures Historical Data.csv": NaturalGasAssetGraphData,
            "graph data/Platinum Futures Historical Data.csv": PlatinumAssetGraphData,
            "graph data/Silver Futures Historical Data.csv": SilverAssetGraphData,
        }

        for file_path, model_class in file_mapping.items():
            self.save_data_to_models(file_path, model_class)

        return Response("Data saved!!", status=status.HTTP_200_OK)
    
    def update_asset_value(self, val , model_class):
    
        troy_ounce_to_gram = 31.1034768
        barral_to_liter = 158.987294928
        mmbtu_to_scm = 25.2

        if model_class in [GoldAssetGraphData,SilverAssetGraphData,CopperAssetGraphData,PlatinumAssetGraphData]:
            val = float(val/troy_ounce_to_gram)

        elif model_class in [OilAssetGraphData]:
            val = float(val/barral_to_liter)
                
        elif model_class in [NaturalGasAssetGraphData]:
            val = float(val/mmbtu_to_scm)
            
    
        return val


    def save_data_to_models(self, file_path, model_class:AxisValue):
        columns_to_drop = ["Change %"]
        df = pd.read_csv(file_path)
        df = df.drop(columns_to_drop, axis=1)
        df['Price'] = df["Price"].apply(lambda x: str(x).replace(",","")).apply(float)
        df['Open'] = df["Open"].apply(lambda x: str(x).replace(",","")).apply(float)
        df['High'] = df["High"].apply(lambda x: str(x).replace(",","")).apply(float)
        df['Low'] = df["Low"].apply(lambda x: str(x).replace(",","")).apply(float)
        df['Vol.'] = df["Vol."].replace(np.nan,"")
        data = df.to_dict(orient="records")
        model_data = [model_class(
            price= self.update_asset_value(item['Price'],model_class),
            open= self.update_asset_value(item['Open'],model_class),
            high= self.update_asset_value(item['High'],model_class),
            low= self.update_asset_value(item['Low'],model_class),
            date= datetime.strptime(item['Date'],"%m/%d/%Y").strftime("%Y-%m-%d"),
            vol=item['Vol.'],
        ) for item in data]
        model_class.objects.all().delete()
        model_class.objects.bulk_create(model_data)
        

class GoldAssetGraphDataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GoldAssetGraphData.objects.all()  # Choose any model, as the fields are the same for all models
    serializer_class = GoldAssetGraphDataSerializer

class SilverAssetGraphDataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SilverAssetGraphData.objects.all()  # Choose any model, as the fields are the same for all models
    serializer_class = SilverAssetGraphDataSerializer

class PlatinumAssetGraphDataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PlatinumAssetGraphData.objects.all()  # Choose any model, as the fields are the same for all models
    serializer_class = PlatinumAssetGraphDataSerializer

class CopperAssetGraphDataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CopperAssetGraphData.objects.all()  # Choose any model, as the fields are the same for all models
    serializer_class = CopperAssetGraphDataSerializer

class OilAssetGraphDataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OilAssetGraphData.objects.all()  # Choose any model, as the fields are the same for all models
    serializer_class = OilAssetGraphDataSerializer

class NaturalGasAssetGraphDataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NaturalGasAssetGraphData.objects.all()  # Choose any model, as the fields are the same for all models
    serializer_class = NaturalGasAssetGraphDataSerializer

