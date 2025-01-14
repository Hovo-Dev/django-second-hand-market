from django.contrib.auth.models import AbstractUser
from django.db import models

class Publisher(AbstractUser):
    address = models.TextField()
    full_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'publisher'

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
