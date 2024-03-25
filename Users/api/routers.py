from django.urls import path
from Users.api.views import UserRegisterView, UserDetailView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('auth/registerUser', UserRegisterView.as_view()),
    path('auth/loginUser', TokenObtainPairView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
    path('auth/me', UserDetailView.as_view())
]