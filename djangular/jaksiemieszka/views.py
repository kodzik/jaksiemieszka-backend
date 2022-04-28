from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from jaksiemieszka.models import User

from jaksiemieszka.models import Comment
from .serializers import CommentSerializer, LocationSerializer, UserSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class UserViews(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"status": "success", "data": serializer.data},status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class CommentViews(APIView):
    def get(self, request, id=None):
        if id:
            item = Comment.objects.get(id=id)
            serializer = CommentSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Comment.objects.all()
        serializer = CommentSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    # def get(self, request, id=None):

    #     items = Comment.objects.all()
    #     serializer = CommentSerializer(items, many=True)
    #     return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        permission_classes = (IsAuthenticated,)

        serializer = CommentSerializer(data=request.data)
        print(serializer.initial_data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class ExampleView(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        user = User.objects.get(username=request.user)
        serializer = UserSerializer(user)
        content = {

            'user': serializer.data,  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)