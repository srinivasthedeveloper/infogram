from types import MethodType
from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework import status

from .serializer import AllPostSerializer, ImageSerializer, TestSerializer

from .models import ImageTest, Post, Test

@api_view(['GET'])
def getRoutes(request):
    routes=[
        {'Endpoint':'/posts','method':'get','body':None,'description':'all posts'},
        {'Endpoint':'/posts/id','method':'get','body':None,'description':'particular post'},
    ]
    return Response(routes)


class AllPosts(APIView):
    parser_classes=(MultiPartParser,FormParser)
    
    def post(self,request,*args,**kwargs):
        serializer=AllPostSerializer(data=request.data,partial=True)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            print("serializer",serializer.errors)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,*args,**kwargs):
        posts=Post.objects.all()
        serializer=AllPostSerializer(posts,many=True,context={'request': request}) #context={'request': request} for getting full/absolute url for files
        return Response(serializer.data)

class UpdatePost(APIView):
    def get(self,request,pk,*args,**kwargs):
            post=Post.objects.get(id=pk)
            serializer=AllPostSerializer(post,many=False,context={'request':request})
            return Response(serializer.data)
    def delete(self,request,pk,*args,**kwargs):
        post=Post.objects.get(id=pk)
        post.delete()
        return Response("Deleted")
    def put(self,request,pk,*args,**kwargs):
        post=Post.objects.get(id=pk)
        serializer=AllPostSerializer(instance=post,data=request.data,partial=True)
        if(serializer.is_valid()):
            print("valid")
            serializer.save()
            print("saved")
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','POST','DELETE'])
def getTestData(request,pk):
    if(request.method=='GET'):
        test=Test.objects.all()
        serializer=TestSerializer(test,many=True,context={'request':request})
        print("get data",serializer.data)
        return Response(serializer.data)
    elif(request.method=='PUT'):
        test=Test.objects.get(id=pk)
        serializer=TestSerializer(instance=test ,data=request.data,partial=True)
        if(serializer.is_valid()):
            print("valid")
            serializer.save()
            print("saved")
            return Response(serializer.data)
        return Response("error",serializer.error,status=400)
    elif(request.method=='POST'):
        serializer=TestSerializer(data=request.data,partial=True)
        if(serializer.is_valid()):
            print("Valid post")
            serializer.save()
            return Response(serializer.data)
        return Response("post error",serializer.error,status=400)
    elif(request.method=='DELETE'):
        test=Test.objects.get(id=pk)
        test.delete()
        return Response("Deleted Successfully")

class ImageView(APIView):
    parser_classes=(MultiPartParser,FormParser)
    
    def post(self,request,*args,**kwargs):
        serializer=ImageSerializer(data=request.data,partial=True)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,*args,**kwargs):
        image=ImageTest.objects.all()
        serializer=ImageSerializer(image,many=True,context={'request':request})
        return Response(serializer.data)

class ImageUpdate(APIView):
    parser_classes=(MultiPartParser,FormParser)

    def put(self,request,pk,*args,**kwargs):
        image=ImageTest.objects.get(id=pk)
        serializer=ImageSerializer(instance=image ,data=request.data,partial=True)
        if(serializer.is_valid()):
            print("valid")
            serializer.save()
            print("saved")
            return Response(serializer.data)
        return Response("error",serializer.error,status=400)

    def delete(self,request,pk,*args,**kwargs):
        image=ImageTest.objects.get(id=pk)
        image.delete()
        return Response("item deleted")

    def get(self,request,pk,*args,**kwargs):
        image=ImageTest.objects.get(id=pk)
        serializer=ImageSerializer(image,many=False,context={"request":request})
        return Response(serializer.data)



# @api_view(['GET','POST'])
# def imageTest(request):
#     if(request.method=='GET'):
#         image=ImageTest.objects.all()
#         serializer=ImageSerializer(image,many=True,context={'request':request})
#         return Response(serializer.data)
#     elif(request.method=='POST'):
#         serializer=ImageSerializer(data=request.data,partial=True)
#         if(serializer.is_valid()):
#             print("valid image post")
#             serializer.save()
#             return Response(serializer.data)
#         return Response("Image error",serializer.error,status=400)
