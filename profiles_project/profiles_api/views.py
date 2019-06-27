from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from profiles_api import serializers
from profiles_api import models


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


class HelloViewSet(viewsets.ViewSet):
    """test api viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        return Response({
            "message": "hello world",
            "data": [
                "Uses actions(list, create, retrieve, update, partial_update, destroy)",
                "Automatically maps to URLs using Routers",
                "Provides more functionality with less code",
            ]
        })

    def create(self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}, you're a cool dude, bro"
            return Response({ "message": message })
        else:
            return Response( serializer.errors, status=400 )

    def retrieve(self, request, pk=None):
        """handle getting an object by its ID"""
        return Response({ "http_method": "GET (by ID)" })

    def update(self, request, pk=None):
        """update an entire object"""
        return Response({ "http_method": "PUT" })

    def partial_update(self, request, pk=None):
        """update only specified parameters on object"""
        return Response({ "http_method": "PATCH" })

    def destoy(self, request, pk=None):
        """delete an object"""
        return Response({ "http_method": "DELETE" })



class UserProfileViewSet(viewsets.ModelViewSet):
    """handle crud actions for user profiles"""
    serializer_class = serializers.USerProfileSerializer    
    queryset = models.UserProfile.objects.all()
