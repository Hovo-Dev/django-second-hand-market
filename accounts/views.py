from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status, generics

from accounts.models import Publisher
from accounts.serializers import PublisherSerializer, CustomTokenObtainPairSerializer
from second_hand_project.mixins import AuthMixin


class RegisterView(CreateAPIView):
    """
       API endpoint for user registration with JWT token return.
    """
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

    def create(self, request, *args, **kwargs):
        """
        Register a new user and return JWT tokens.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Save the user
        user = serializer.save()

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)

        # Return success response
        return Response({
            "detail": "User registered successfully.",
            "user": serializer.data,
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }, status=status.HTTP_201_CREATED)

class LoginTokenObtainPairView(TokenObtainPairView):
    """
    Returns JWT access and refresh tokens upon successful login.
    """
    serializer_class = CustomTokenObtainPairSerializer

class ProfileDetailView(AuthMixin, generics.RetrieveAPIView):
    """
    Fetches the details of the authenticated user.
    """
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

    def get_object(self):
        return self.request.user
