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
            serializer = DataSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                response_data.append(serializer.data)
            else:
                response_data.append(serializer.errors)

        return Response(response_data, status=status.HTTP_201_CREATED)
