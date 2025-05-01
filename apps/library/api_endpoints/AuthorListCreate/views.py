from .serializers import AuthorListSerializer, AuthorCreateSerializer
from apps.library.models import Author
from rest_framework.generics import ListCreateAPIView
from apps.users.permissions import IsAdminRole


class AuthorListCreateView(ListCreateAPIView):
    queryset = Author.objects.all()

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (IsAdminRole,)
        return super().get_permissions()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AuthorCreateSerializer
        return AuthorListSerializer


__all__ = [
    'AuthorListCreateView',
]
