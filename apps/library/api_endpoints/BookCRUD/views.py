from .serializers import BookDetailSerializer, BookUpdateSerializer
from apps.library.models import Book
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from apps.users.permissions import IsAdminRole
from rest_framework.parsers import MultiPartParser


class BookRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    http_method_names = ('get', 'patch', 'delete')
    parser_classes = (MultiPartParser,)

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return BookUpdateSerializer
        return BookDetailSerializer

    def get_permissions(self):
        if self.request.method == 'PATCH' or self.request.method == 'DELETE':
            self.permission_classes = (IsAdminRole,)
        return super().get_permissions()


__all__ = [
    'BookRetrieveUpdateDestroyView',
]
