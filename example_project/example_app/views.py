from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class ExampleView(APIView):
    def get(self, request, format=None):
        return Response({
            "message": "hello from the rest framework!!!",
            "data": ["the", "rest", "framework", "is", "cool!"]
        })
