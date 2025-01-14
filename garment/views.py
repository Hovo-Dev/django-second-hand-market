from second_hand_project.mixins import AuthMixin
from second_hand_project.pagination import StandardResultsSetPagination

from garment.models import Garment
from garment.serializers import GarmentSerializer

from rest_framework.exceptions import PermissionDenied, NotFound
from rest_framework.response import Response
from rest_framework import status, generics

class GetGarmentListView(generics.ListAPIView):
    queryset = Garment.objects.all()
    serializer_class = GarmentSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        """
        Customize the queryset to apply filtering based on request query parameters.
        """
        queryset = Garment.objects.all()

        # Get filter parameters from the request
        size = self.request.query_params.get('size')
        garment_type = self.request.query_params.get('type')
        price_min = self.request.query_params.get('price_min')
        price_max = self.request.query_params.get('price_max')

        # Apply filtering
        if size:
            queryset = queryset.filter(size=size)
        if garment_type:
            queryset = queryset.filter(type=garment_type)
        if price_min:
            queryset = queryset.filter(price__gte=price_min)
        if price_max:
            queryset = queryset.filter(price__lte=price_max)

        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()  # Use the filtered queryset
        page = self.paginate_queryset(queryset)

        # Check if the page is empty to use default pagination options
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class GetGarmentDetailView(generics.RetrieveAPIView):
    """
    Retrieve the details of a specific garment.
    """
    queryset = Garment.objects.all()
    serializer_class = GarmentSerializer
    lookup_field = 'id'

class CreateGarmentView(AuthMixin, generics.CreateAPIView):
    """
    Create a new garment.
    """
    def post(self, request, *args, **kwargs):
        serializer = GarmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(publisher=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class DeleteGarmentView(AuthMixin, generics.DestroyAPIView):
    """
    Delete a garment.
    """
    queryset = Garment.objects.all()
    serializer_class = GarmentSerializer
    lookup_field = 'id'

    def get_object(self):
        # Fetch the garment based on the provided ID
        garment = super().get_object()

        # Check if the garment belongs to the requesting user
        if garment.publisher != self.request.user:
            raise PermissionDenied("You do not have permission to delete this garment.")

        return garment

    def delete(self, request, *args, **kwargs):
        # Call the custom get_object method
        instance = self.get_object()

        # Delete the garment instance
        instance.delete()

        return Response({'detail': 'Garment deleted successfully.'}, status=status.HTTP_200_OK)

class UpdateGarmentView(AuthMixin, generics.UpdateAPIView):
    """
    Update a specific garment.
    """
    queryset = Garment.objects.all()
    serializer_class = GarmentSerializer
    lookup_field = 'id'

    def get_object(self):
        # Fetch the garment based on the provided ID
        garment = super().get_object()

        # Check if the garment belongs to the requesting user
        if garment.publisher != self.request.user:
            raise PermissionDenied("You do not have permission to update this garment.")

        return garment
