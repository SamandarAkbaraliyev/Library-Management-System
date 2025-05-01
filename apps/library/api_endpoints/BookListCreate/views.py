from .serializers import BookListSerializer, BookCreateSerializer
from apps.library.models import Book
from rest_framework.generics import ListCreateAPIView
from apps.users.permissions import IsAdminRole
from rest_framework.parsers import MultiPartParser


class BookListCreateView(ListCreateAPIView):
    queryset = Book.objects.all()
    parser_classes = (MultiPartParser,)

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (IsAdminRole,)
        return super().get_permissions()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookCreateSerializer
        return BookListSerializer


__all__ = [
    'BookListCreateView',
]
