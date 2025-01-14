from garment.views import GetGarmentListView, GetGarmentDetailView, DeleteGarmentView, CreateGarmentView, UpdateGarmentView
from django.urls import path

urlpatterns = [
    path('create/', CreateGarmentView.as_view(), name='create_garment'),
    path('list/', GetGarmentListView.as_view(), name='get_paginated_garment'),

    path('<int:id>/', GetGarmentDetailView.as_view(), name='get_garment_detail'),
    path('<int:id>/delete/', DeleteGarmentView.as_view(), name='delete_garment'),

    path('<int:id>/update/', UpdateGarmentView.as_view(), name='update_garment'),
]
