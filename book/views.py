from django.shortcuts import render
from rest_framework import generics

from book.models import Book
from book.serializers import BookModelSerializers


class BookApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializers
