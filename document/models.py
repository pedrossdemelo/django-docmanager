import uuid
from datetime import datetime
from django.db import models
from user.models import User
from .countries import COUNTRIES
from .timezones import TIMEZONES


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    locale = models.CharField(max_length=2, choices=COUNTRIES, default="BR")
    timezone = models.CharField(max_length=11, choices=TIMEZONES, default="(UTC-03:00)")
    lang = models.CharField(
        max_length=2,
        choices=[("en", "English"), ("es", "Español"), ("pt", "Português")],
        default="pt",
    )
    users = models.ManyToManyField(User, related_name="companies")
    # created_by doesn't fit in here, because we can transfer ownership
    admin = models.OneToOneField(
        User, related_name="admin_of", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "company"


class Doc(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    date_limit_to_sign = models.DateTimeField()
    signed = models.BooleanField(default=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="docs")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="docs")

    def __str__(self):
        return f"{self.company} by {self.created_by} @ {self.created_at}"

    class Meta:
        db_table = "doc"
