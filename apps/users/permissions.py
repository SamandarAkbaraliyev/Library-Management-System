from rest_framework.permissions import IsAuthenticated


class IsAdminRole(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.role == 'admin'
