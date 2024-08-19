from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers, models
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

class HelloApiView(APIView):
    
    serializer_class = serializers.HelloSerializer
    
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
        
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'HELLO {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )
            
    def put(self,request,pk=None):
        return Response({'method':'PUT'})
    
    def patch(self,request,pk=None):
        return Response({'method':'PATCH'})
    
    def delete(self,request,pk=None):
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    
    serializer_class=serializers.HelloSerializer
    
    def list(self, request):
        a_viewset=[
            'Uses actions: list, create, retrieve, update, partial_update',
            'Automatically maps to URLs using routers',
            'Provides more functionality with less code',
        ]

        return Response({'message':'Hello!', 'a_viewset:':a_viewset})
    
    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name= serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message ': message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self,request,pk=None):
        return Response({'http_method':'GET'})
    
    def update(self,request,pk=None):
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        return Response({'http_method':'DELETE'})


class  UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset= models.UserProfile.objects.all()


class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES