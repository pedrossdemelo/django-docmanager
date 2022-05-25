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

    # disallow updates to the "signed" field after it has been set to true
    def update(self, instance, validated_data):
        if instance.signed:
            validated_data.pop("signed", None)
        return super().update(instance, validated_data)

class CompanySerializer(serializers.ModelSerializer):
    users = serializers.SlugRelatedField(
        slug_field="email", many=True, allow_null=False, queryset=User.objects.all()
    )

    admin = serializers.SlugRelatedField(
        slug_field="email", allow_null=False, queryset=User.objects.all()
    )

    class Meta:
        model = Company
        fields = "__all__"
