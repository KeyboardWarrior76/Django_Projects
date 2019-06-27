from rest_framework.views import APIView
from rest_framework.response import Response

from profiles_api import serializers


class HelloApiView(APIView):
    """test api view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """returns a list of APIView features"""
        return Response({
            "message": "hello world!",
            "data": [
                "Uses HTTP methods as functions (get, post, put, patch, delete)",
                "Is similar to a traditional Django View",
                "Gives you the most control over application logic",
                "Is mapped manually to URLS",
            ],
        })

    def post(self, request):
        """create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}, you're a cool dude, bro"
            return Response({ "message": message })
        else:
            return Response( serializer.errors, status=400 )


    def put(self, request, pk=None):
        """handle updating an object"""
        return Response({"method": "PUT"})

    def patch(self, request, pk=None):
        """Handle a partial update on an object"""
        return Response({ "method": "PATCH" })

    def delete(self, request, pk=None):
        """deletes an object"""
        return Response({ "method": "DELETE" })