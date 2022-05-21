from rest_framework import serializers
from .models import User
from document.models import Company


class UserSerializer(serializers.ModelSerializer):
    admin_of = serializers.SlugRelatedField(
        slug_field="name", allow_null=True, queryset=Company.objects.all()
    )
    companies = serializers.SlugRelatedField(
        slug_field="name", many=True, queryset=Company.objects.all()
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
