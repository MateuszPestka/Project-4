from django.db import models

# Create your models here.


class Booking(models.Model):
    first_name = models.charField("your first name", max_length=100)
    last_name = models.charField("your last name", max_length=100)
    email = models.EmailField()
    mobile = models.IntegerField(max_length=13)
    created_on = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    time = models.TimeField()
    special_requirements = models.TextField()
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["time"]
