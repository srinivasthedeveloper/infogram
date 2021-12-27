from django.db.models import fields
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from drf_writable_nested import WritableNestedModelSerializer
from .models import Demo, ImageTest, Post,Comment, Test

class AllCommentsSerializer(ModelSerializer):
    class Meta:
        model=Comment
        fields="__all__"

        
class AllPostSerializer(WritableNestedModelSerializer,ModelSerializer): #writablenestedmodelserializer for creation of nested data like comments
    comment = AllCommentsSerializer(many=True) #for forign key models [refer the same name for variable and related_name in modles]
    class Meta:
        model=Post
        # fields=['id','username','location','caption'] or
        fields='__all__'

class DemoSerializer(ModelSerializer):
    class Meta:
        model=Demo
        fields="__all__"

class TestSerializer(WritableNestedModelSerializer,ModelSerializer):
    demo=DemoSerializer(many=True)
    class Meta:
        model=Test
        fields="__all__"

class ImageSerializer(ModelSerializer):
    class Meta:
        model=ImageTest
        fields="__all__"