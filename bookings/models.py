from django.db import models
from django.contrib.auth.models import User
from package.models import Package
# Create your models here.

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    number_of_people = models.PositiveIntegerField(default=1)
    booking_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Booking {self.id} by {self.user.username} for {self.package.name}"