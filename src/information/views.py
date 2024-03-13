from django.shortcuts import render
from rest_framework.generics import ListAPIView,ListCreateAPIView
from .models import Book, Author
from information import serializers


class BookListAPIView(ListCreateAPIView):
    queryset = Book.objects.select_related()
    serializer_class = serializers.BookSerializer


class AuthorListAPIView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorSerializer