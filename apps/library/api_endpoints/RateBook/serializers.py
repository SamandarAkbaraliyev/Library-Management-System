from rest_framework import serializers
from apps.library.models import Rating


class RateBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = (
            'id',
            'rating'
        )

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        validated_data['book_id'] = self.context['book']
        rating = Rating.objects.create(**validated_data)
        return rating
