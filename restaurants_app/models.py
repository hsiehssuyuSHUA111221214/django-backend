from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class RestaurantReview(models.Model):
    # 基本資訊
    restaurant_name = models.CharField(max_length=255, verbose_name="餐廳名稱")
    food_type = models.CharField(max_length=255, verbose_name="美食種類")
    address = models.TextField(verbose_name="餐廳地址")
    is_google_maps_verified = models.BooleanField(default=False, verbose_name="Google Maps 驗證")
    
    # 評分項目 (1-5星)
    taste_rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="餐點風味"
    )
    speed_rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="出餐速度"
    )
    cleanliness_rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="環境衛生"
    )
    service_rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="服務態度"
    )
    
    # 餐廳服務選項 (二選一)
    DELIVERY_CHOICES = [
        ('yes', '有提供外送'),
        ('no', '無提供外送'),
    ]
    delivery_service = models.CharField(
        max_length=3,
        choices=DELIVERY_CHOICES,
        verbose_name="外送服務"
    )

    PAYMENT_CHOICES = [
        ('yes', '有多元支付'),
        ('no', '無多元支付'),
    ]
    multiple_payment = models.CharField(
        max_length=3,
        choices=PAYMENT_CHOICES,
        verbose_name="多元支付"
    )

    APP_CHOICES = [
        ('yes', '有預點APP'),
        ('no', '無預點APP'),
    ]
    preorder_app = models.CharField(
        max_length=3,
        choices=APP_CHOICES,
        verbose_name="預點APP"
    )

    DINE_IN_CHOICES = [
        ('yes', '有內用空間'),
        ('no', '無內用空間'),
    ]
    dine_in_space = models.CharField(
        max_length=3,
        choices=DINE_IN_CHOICES,
        verbose_name="內用空間"
    )

    MENU_CHOICES = [
        ('yes', '有電子菜單'),
        ('no', '無電子菜單'),
    ]
    electronic_menu = models.CharField(
        max_length=3,
        choices=MENU_CHOICES,
        verbose_name="電子菜單"
    )

    # 評論內容
    review = models.TextField(verbose_name="評論內容")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="建立時間")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新時間")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "美食評論"
        verbose_name_plural = "美食評論"

    def __str__(self):
        return f"{self.restaurant_name} - 風味:{self.taste_rating}⭐ 速度:{self.speed_rating}⭐ 衛生:{self.cleanliness_rating}⭐ 服務:{self.service_rating}⭐"

    @property
    def average_rating(self):
        """計算平均評分"""
        ratings = [self.taste_rating, self.speed_rating, self.cleanliness_rating, self.service_rating]
        return sum(ratings) / len(ratings)
