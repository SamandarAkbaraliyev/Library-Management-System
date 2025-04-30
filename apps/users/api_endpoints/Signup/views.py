from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializer


class SignupView(CreateAPIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


__all__ = [
    'SignupView'
]
