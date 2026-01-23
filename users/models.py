# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

PHONE_REGEX = RegexValidator(
    regex=r'^\+?\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
)

class User(AbstractUser):
    # Remove username requirement and use email as unique identifier
    username = None
    email = models.EmailField('email address', unique=True)

    USER_TYPE_CHOICES = (
        ('passenger', 'Passenger'),
        ('rider', 'Rider'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='passenger')
    phone = models.CharField(validators=[PHONE_REGEX], max_length=16, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email} ({self.get_user_type_display()})"
