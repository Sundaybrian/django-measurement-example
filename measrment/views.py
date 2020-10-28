from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from . serializers import MeasurementSerializer
from rest_framework import status
from measurement.measures import Distance
from .models import Measurement
import json
# Create your views here.

class MeasurementAPI(APIView):
    def get(self, request, format=None):
        all_merch = Measurement.objects.all()
        serializers = MeasurementSerializer(all_merch, many=True)
        return Response(serializers.data)
    #     pass
    def post(self, request, format=None):
        serializers = MeasurementSerializer(data=request.data)
        if serializers.is_valid():
            # do save since we dont need the data
            val = serializers.validated_data.get('val')
            unit1 = serializers.validated_data.get('unit_1')
            unit2 = serializers.validated_data.get('unit_2')
            outputStr=f'Distance({unit1}={val}).{unit2}'

            conversion = {
                "output":eval(outputStr)
                }

            res = json.dumps(conversion)
            return Response(res, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) 
