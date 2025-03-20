from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username  # ✅ 確保這裡是 `self.username`

class RestaurantReview(models.Model):
    restaurant_name = models.CharField(max_length=255)
    address = models.TextField()
    review = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.restaurant_name} - {self.rating}⭐"




