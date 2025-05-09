from .serializers import BookListSerializer, BookCreateSerializer
from apps.library.models import Book
from rest_framework.generics import ListCreateAPIView
from apps.users.permissions import IsAdminRole
from rest_framework.parsers import MultiPartParser
from drf_spectacular.utils import extend_schema


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

    @extend_schema(
        request=BookCreateSerializer,
        responses={201: BookCreateSerializer},
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


__all__ = [
    'BookListCreateView',
]
