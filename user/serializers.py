from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    admin_of = serializers.SlugRelatedField(
        slug_field="name", read_only=True, allow_null=True
    )
    companies = serializers.SlugRelatedField(
        slug_field="name",
        many=True,
        read_only=True,
    )

    class Meta:
        model = User
        fields = [
            "email",
            "email_verified",
            "created_at",
            "last_update_at",
            "admin_of",
            "companies",
        ]
