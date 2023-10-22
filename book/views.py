from django.shortcuts import render
from rest_framework import generics

from book.models import Book
from book.serializers import BookModelSerializers


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializers


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializers


class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializers


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializers

