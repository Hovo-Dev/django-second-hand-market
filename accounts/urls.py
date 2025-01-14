from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView

from .views import RegisterView, ProfileDetailView, LoginTokenObtainPairView

urlpatterns = [
    path('login/', LoginTokenObtainPairView.as_view(), name='login'),
    path('logout/', TokenBlacklistView.as_view(), name='logout'),
    path('me/', ProfileDetailView.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='register'),

    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
]
