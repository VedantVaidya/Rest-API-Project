from django.shortcuts import render
from rest_framework.generics import ListAPIView,ListCreateAPIView, CreateAPIView
from .models import Book, Author
from information import serializers, services


class BookListAPIView(ListAPIView):
    queryset = Book.objects.select_related()
    serializer_class = serializers.BookSerializer


class AuthorListAPIView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorSerializer


class SendMailAPIView(CreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = serializers.MailSerializer

    def create(self, request, *args, **kwargs):
        to=request.data.get("to")
        subject=request.data.get("subject")
        body=request.data.get("body")
        return services.send_mail_func(to,subject,body)
        






















# from django.views import View
# import io
# from rest_framework.parsers import JSONParser
# from rest_framework.renderers import JSONRenderer
# from django.http import HttpResponse
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt

# @method_decorator(csrf_exempt, name = "dispatch")
# class Test(View):
#     def post(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_dict = JSONParser().parse(stream)
#         serializer = serializers.AuthorSerializer(data=python_dict)
#         if serializer.is_valid():
#             serializer.save()
#             res = {"detail":"Data Created"}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type="application/json")
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type="application/json")
    

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# class Test(APIView):
#     def post(self, request, format=None):
#         serializer = serializers.AuthorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"detail":"Data Created"}, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import CreateModelMixin

# class Test(GenericAPIView, CreateModelMixin):
#     queryset = Author.objects.all()
#     serializer_class = serializers.AuthorSerializer
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    

# from rest_framework.generics import CreateAPIView
    
# class Test(CreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = serializers.AuthorSerializer
