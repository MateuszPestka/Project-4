from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Booking(models.Model):
    first_name = models.CharField("your first name", max_length=100)
    last_name = models.CharField("your last name", max_length=100)
    email = models.EmailField()
    mobile = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    time = models.TimeField()
    special_requirements = models.TextField()
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["time"]
