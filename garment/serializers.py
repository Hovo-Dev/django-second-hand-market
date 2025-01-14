from accounts.serializers import PublisherSerializer
from garment.models import Garment
from rest_framework import serializers

class GarmentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Garment model.
    """
    price = serializers.FloatField() # Converts Decimal to flat in JSON-serializable format
    publisher = PublisherSerializer(read_only=True)

    class Meta:
        model = Garment
        fields = ['id', 'size', 'price', 'type', 'description', 'publisher']
