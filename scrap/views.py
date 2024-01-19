from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .seralizers import *

# Create your views here.
class ScrapAPI(APIView):
    def post(self, request, format=None):
        all_data = request.data
        response_data = []
        for data in all_data:
            exist_data = {
                'ip_address': data['ip_address'],
                'port': data['port'],
                'country':data['country'],
                'protocols':data['protocols']
            }
            existing_record = JobData.objects.filter(**exist_data).first()
            if existing_record:
                response_data.append({'message': 'Record already exists'})
            else:
                serializer = DataSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    response_data.append(serializer.data)
                else:
                    response_data.append(serializer.errors)

        return Response(response_data, status=status.HTTP_201_CREATED)
