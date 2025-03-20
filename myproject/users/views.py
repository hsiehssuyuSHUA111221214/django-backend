from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from django.db.models import Q
from rest_framework import serializers
from users.models import RestaurantReview

class RestaurantReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantReview
        fields = '__all__'

from django.db import models

class RestaurantReview(models.Model):
    restaurant_name = models.CharField(max_length=255)
    address = models.TextField()
    review = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.restaurant_name

User = get_user_model()


from users.serializers import UserSerializer, LoginSerializer
from users.models import RestaurantReview

class SignUpView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class SignInView(TokenObtainPairView):
    serializer_class = LoginSerializer


@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def search_restaurant(request):
    query = request.GET.get("q", "").strip()  # 去除首尾空格，避免空查詢

    if not query:
        return Response({"message": "請輸入店名或地址"}, status=400)

    restaurants = RestaurantReview.objects.filter(
        Q(restaurant_name__icontains=query) | Q(address__icontains=query)
    )

    if not restaurants.exists():
        return Response({"message": "找不到符合的餐廳"}, status=404)

    serializer = RestaurantReviewSerializer(restaurants, many=True)
    return Response(serializer.data)
