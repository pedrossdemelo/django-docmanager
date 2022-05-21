from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    last_password_redefinition_at = models.DateTimeField(auto_now=True)
    email_verified = models.BooleanField(default=False)
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(sef):
        return sef.email

    class Meta:
        db_table = "user"
