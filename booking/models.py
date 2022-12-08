from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Booking(models.Model):
    first_name = models.CharField("your first name", max_length=50)
    last_name = models.CharField("your last name", max_length=50)
    email = models.EmailField()
    mobile = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    time = models.TimeField()
    group_size = models.PositiveIntegerField(default=1)
    special_requirements = models.TextField(blank=True)
    approved = models.BooleanField(default=False)
    vip = models.BooleanField(default=False)

    class Meta:
        ordering = ["time"]

    def __str__(self):
        return f"{self.time}: {self.first_name} {self.last_name}"
