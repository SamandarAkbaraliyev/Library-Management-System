from rest_framework import serializers
from apps.library.models import Author
from apps.library.api_endpoints.AuthorListCreate.serializers import BookAuthorSerializer


class AuthorDetailSerializer(serializers.ModelSerializer):
    books = BookAuthorSerializer(many=True, source='book_set')

    class Meta:
        model = Author
        fields = (
            'id',
            'first_name',
            'last_name',
            'birth_date',
            'death_date',
            'books',
        )


class AuthorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'id',
            'first_name',
            'last_name',
            'birth_date',
            'death_date',
        )