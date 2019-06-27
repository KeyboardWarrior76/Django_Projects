from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """test api view"""

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

    def post(self, request, format=None):
        print(request)
        return Response({
            "message": "data recieved"
        })
