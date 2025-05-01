from .serializers import AuthorDetailSerializer, AuthorUpdateSerializer
from apps.library.models import Author
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from apps.users.permissions import IsAdminRole


class AuthorCRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    http_method_names = ('get', 'patch', 'delete')

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return AuthorUpdateSerializer
        return AuthorDetailSerializer

    def get_permissions(self):
        if self.request.method == 'PATCH' or self.request.method == 'DELETE':
            self.permission_classes = (IsAdminRole,)
        return super().get_permissions()


__all__ = [
    'AuthorCRUDView'
]
