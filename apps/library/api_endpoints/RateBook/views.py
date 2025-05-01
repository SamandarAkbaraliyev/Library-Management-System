from .serializers import RateBookSerializer
from apps.library.models import Rating
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class RateBookView(CreateAPIView):
    serializer_class = RateBookSerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['book'] = self.kwargs['pk']
        return context

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rating = serializer.save()

        return Response({
            "user": str(rating.user.id),
            "book": rating.book.id,
            "rating": rating.rating
        }, status=status.HTTP_201_CREATED)


__all__ = [
    'RateBookView'
]
