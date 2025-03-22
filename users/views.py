from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, '兩次輸入的密碼不一致')
            return redirect('register')

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, '用戶名已被使用')
            return redirect('register')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, '電子信箱已被使用')
            return redirect('register')

        try:
            user = CustomUser.objects.create_user(
                username=username,
                email=email,
                password=password1
            )
            login(request, user)
            messages.success(request, '註冊成功！歡迎加入美食評論系統')
            return redirect('home')
        except Exception as e:
            messages.error(request, f'註冊失敗：{str(e)}')
            return redirect('register')

    return render(request, 'registration/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, '登入成功！')
            return redirect('home')
        else:
            messages.error(request, '用戶名或密碼錯誤')
            return redirect('login')
    
    return render(request, 'registration/login.html')

@login_required
def user_profile(request):
    return render(request, 'registration/profile.html', {
        'user': request.user
    })
