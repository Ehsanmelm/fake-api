from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import requests

# Create your views here.

class GetDataView(APIView):

    def get(self, request):
        url = 'https://api.beeaab.com/fa/weblog/blog/'
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            return Response(data)
        else:
            return Response(data)
  