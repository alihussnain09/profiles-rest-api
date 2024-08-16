from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    def get(self,request,format=None):
        an_apiview = [
            'Uses HTTP Functions',
            'similar to traditional django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]
        return Response({
            'message': 'Hello!',
            'an_apiview' : an_apiview
            })
