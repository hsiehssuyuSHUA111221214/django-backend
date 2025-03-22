from django import forms
from .models import RestaurantReview

class ReviewForm(forms.ModelForm):
    class Meta:
        model = RestaurantReview
        fields = [
            'restaurant_name', 
            'food_type', 
            'address', 
            'taste_rating',
            'speed_rating',
            'cleanliness_rating',
            'service_rating',
            'delivery_service',
            'multiple_payment',
            'preorder_app',
            'dine_in_space',
            'electronic_menu',
            'review'
        ]
        widgets = {
            'restaurant_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入餐廳名稱'}),
            'food_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '例如：台式、日式、韓式...'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入餐廳地址'}),
            'taste_rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
            'speed_rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
            'cleanliness_rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
            'service_rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
            'delivery_service': forms.Select(attrs={'class': 'form-select'}),
            'multiple_payment': forms.Select(attrs={'class': 'form-select'}),
            'preorder_app': forms.Select(attrs={'class': 'form-select'}),
            'dine_in_space': forms.Select(attrs={'class': 'form-select'}),
            'electronic_menu': forms.Select(attrs={'class': 'form-select'}),
            'review': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': '請寫下您的評論'}),
        }
        labels = {
            'restaurant_name': '餐廳名稱',
            'food_type': '餐廳類型',
            'address': '地址',
            'taste_rating': '口味評分',
            'speed_rating': '速度評分',
            'cleanliness_rating': '整潔評分',
            'service_rating': '服務評分',
            'delivery_service': '外送服務',
            'multiple_payment': '多種付款方式',
            'preorder_app': '預約應用程式',
            'dine_in_space': '內用空間',
            'electronic_menu': '電子菜單',
            'review': '評論內容',
        }
