from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """ Test API VIEW """
    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        """ returns a list of APIView features """
        return Response({ 
            "message": "hello", 
            "apiview": [
                "Uses HTTP methods as function (get, post, patch, put, delete)",
                "Is similar to a traditional Django View",
                "Gives you the most control over application logic",
                "Is mapped manually to URLS",
            ]
        })

    
    def post(self, request, format=None):
        """ Create a hello message with our name """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"
            return Response({ "message": message })
        else:
            return Response(serializer.errors, status=400)