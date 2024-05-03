from django.db import models
from django.contrib.auth.models import User
# Log passwords
class PasswordLogger(models.Model):
    password = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField()

    def __str__(self):
        return f"Password Attempt: {self.password} - {'Success' if self.success else 'Failure'}"