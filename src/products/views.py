from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from .models import Product
from .serializers import ProductSerializer

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["price", "created_at"]
    ordering = ["-created_at"]  