from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True)
    last_password_redefinition_at = models.DateTimeField(auto_now=True)
    email_verified = models.BooleanField(default=False)
    password = models.CharField(max_length=20, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(s):
        return s.email

    class Meta:
        db_table = "user"
