from rest_framework import serializers
from apps.library.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'id',
            'first_name',
            'last_name',
            'birth_date',
            'death_date',
        )
