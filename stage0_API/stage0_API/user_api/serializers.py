from dataclasses import fields
from turtle import mode
from  rest_framework import serializers
from .models import User_details


class User_detailSerializer(serializers.ModelSerializer):
    objects_id = serializers.IntegerField(required=False, allow_null=True)
    content_type = serializers.CharField(required=False, allow_null=True)
    
    class Meta:
        model = User_details
        fields = "__all__"