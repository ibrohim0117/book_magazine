from rest_framework import serializers

from book.models import Book


class BookModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
