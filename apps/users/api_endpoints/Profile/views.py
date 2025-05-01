from .serializers import ProfileSerializer
from apps.users.models import User
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated


class ProfileView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


__all__ = [
    'ProfileView'
]
