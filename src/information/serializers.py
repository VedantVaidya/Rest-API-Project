from rest_framework import serializers
from information import models


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = models.Book
        fields = ['id','title','page_no','author']
