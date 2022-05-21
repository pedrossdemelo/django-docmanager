from django.utils import timezone
from rest_framework import serializers
from .models import Doc, Company
from user.models import User


class DocumentSerializer(serializers.ModelSerializer):
    company = serializers.SlugRelatedField(
        slug_field="name", allow_null=False, queryset=Company.objects.all()
    )

    created_by = serializers.SlugRelatedField(
        slug_field="email", allow_null=False, queryset=User.objects.all()
    )

    expired = serializers.SerializerMethodField()

    class Meta:
        model = Doc
        fields = [
            "id",
            "created_at",
            "last_update_at",
            "date_limit_to_sign",
            "signed",
            "company",
            "created_by",
            "expired"
        ]

    def get_expired(self, obj):
        return obj.date_limit_to_sign < timezone.now()


class CompanySerializer(serializers.ModelSerializer):
    users = serializers.SlugRelatedField(
        slug_field="email", many=True, read_only=True, allow_null=False
    )

    admin = serializers.SlugRelatedField(
        slug_field="email", allow_null=False, queryset=User.objects.all()
    )

    class Meta:
        model = Company
        fields = "__all__"
