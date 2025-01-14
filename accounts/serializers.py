from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.contrib.auth.password_validation import validate_password

from .models import Publisher

class PublisherSerializer(serializers.ModelSerializer):
    """
    Serializer for customizing Publisher model.
    """
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )

    class Meta:
        model = Publisher
        fields = ['id', 'full_name', 'username', 'address', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Serializer for customizing the token response.
    """
    @classmethod
    def get_token(cls, user):
        """
        Add custom claims to the token.
        """
        token = super().get_token(user)
        token['username'] = user.username

        return token

    def validate(self, attrs):
        """
        Customize the response to include user details.
        """
        data = super().validate(attrs)
        data['user'] =  PublisherSerializer(self.user).data

        return data
