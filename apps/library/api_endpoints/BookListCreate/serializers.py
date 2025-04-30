from rest_framework import serializers
from apps.library.models import Book
from apps.library.serializers import AuthorSerializer


class BookListSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    genre = serializers.CharField(source='genre.name', allow_null=True)
    cover = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = (
            'id',
            'author',
            'title',
            'description',
            'genre',
            'length',
            'published_date',
            'created_at',
            'copies_sold',
            'price',
            'discount',
            'cover',
        )

    def get_cover(self, obj):
        if self.cover:
            return self.context.get('request').build_absolute_uri(self.cover)
        return None


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'id',
            'author',
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
