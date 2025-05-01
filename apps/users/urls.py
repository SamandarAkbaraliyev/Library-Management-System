from django.urls import path
from apps.users import api_endpoints
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path("signup/", api_endpoints.SignupView.as_view(), name="signup"),
    path('login/', api_endpoints.LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("me/", api_endpoints.ProfileView.as_view(), name="profile"),
]

