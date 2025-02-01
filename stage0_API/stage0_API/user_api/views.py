from pickle import TRUE
from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import User_details
from .serializers import User_detailSerializer
# from stage0Task.stage0_API.stage0_API.user_api import serializers


# Create your views here.
class User_detailsView(ViewSet):
    queryset = User_details.objects.all()
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    
    """Handles GET request to retrieve all user details"""
    def list(self, request):
        queryset = User_details.objects.all()
        serializer = User_detailSerializer(queryset, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    """Handles POST request to create a new user detail"""
    # @action(methods= ['post'], detail=False, url_path="user_detail_create")
    def create(self, request):
        print("Raw Request Data:", request.body)  # Check raw body
            
        print("Parsed Data:", request.data)
        serializers = User_detailSerializer(data = request.data)
        try:
            if serializers.is_valid():
                print("Serializer is valid!") 
                email_address =  serializers.validated_data["email_address"]
                github_url = serializers.validated_data["github_url"]
                
                instance = serializers.save()
                if instance is None:
                    return Response({"error": "Failed to save the instance"}, status=status.HTTP_400_BAD_REQUEST)

                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)
        except  Exception as e:
            
            
            print("Exception in create():", str(e))  # Catch any unexpected errors
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    """Handles GET request to retrieve a specific user detail by ID"""
    # @action(methods="get", detail=False) 
    def retrieve(self, request, pk = None):
        try:
            queryset = User_details.objects.all( )
            user = get_object_or_404(queryset, pk = pk)
            serializer = User_detailSerializer(user)
            return Response(serializer.data, status= status.HTTP_200_OK)
        except User_details.DoesNotExist:
            return Response(serializer.errors, status= status.HTTP_404_NOT_FOUND)
        
    
        
        
        
        
            