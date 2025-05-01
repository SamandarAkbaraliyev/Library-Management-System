from rest_framework.generics import DestroyAPIView
from apps.library.models import Genre
from apps.users.permissions import IsAdminRole


class GenreDeleteView(DestroyAPIView):
    queryset = Genre.objects.all()
    permission_classes = (IsAdminRole,)

__all__ = [
    'GenreDeleteView'
]