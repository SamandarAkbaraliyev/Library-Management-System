from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializer
from apps.users.models import User


class SignupView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "status": "success",
            "user": {
                "id": str(user.id),
                "name": user.name,
                "email": user.email,
                "password_set": True
            }
        }, status=status.HTTP_201_CREATED)


__all__ = [
    'SignupView'
]
