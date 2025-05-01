from rest_framework import serializers
from apps.library.models import Author, Book


class BookAuthorSerializer(serializers.ModelSerializer):
    genre = serializers.CharField(source='genre.name', allow_null=True)
    cover = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'description',
            'genre',
            'length',
            'published_date',
            'created_date',
            'copies_sold',
            'price',
            'discount',
            'cover',
        )

    def get_cover(self, obj):
        if obj.cover:
            return self.context.get('request').build_absolute_uri(obj.cover)
        return None


class AuthorListSerializer(serializers.ModelSerializer):
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


class AuthorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'id',
            'first_name',
            'last_name',
            'birth_date',
            'death_date',
        )
