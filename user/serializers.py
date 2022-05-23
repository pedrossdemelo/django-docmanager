from rest_framework import serializers
from .models import User
from document.models import Company


class UserSerializer(serializers.ModelSerializer):
    admin_of = serializers.SlugRelatedField(
        slug_field="name",
        allow_null=True,
        required=False,
        queryset=Company.objects.all(),
    )
    companies = serializers.SlugRelatedField(
        slug_field="name", many=True, required=False, queryset=Company.objects.all()
    )

    class Meta:
        model = User
        fields = [
            "name",
            "id",
            "email",
            "email_verified",
            "created_at",
            "last_update_at",
            "admin_of",
            "companies",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}
