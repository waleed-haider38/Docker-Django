from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price", "is_active", "created_at"]
        read_only_fields = ["id", "created_at"]

        def validate_name(self, value):
            if len(value) < 3:
                 serializers.ValidationError("Name must be at least 3 characters.")
            return value