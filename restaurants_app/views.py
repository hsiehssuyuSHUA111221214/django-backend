from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import RestaurantReview
from .forms import ReviewForm

# Create your views here.

def review_list(request):
    reviews = RestaurantReview.objects.all().order_by('-id')
    return render(request, 'restaurants_app/review_list.html', {
        'reviews': reviews
    })

def review_detail(request, pk):
    review = get_object_or_404(RestaurantReview, pk=pk)
    return render(request, 'restaurants_app/review_detail.html', {
        'review': review
    })

@login_required
def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            messages.success(request, '評論已成功發布！')
            return redirect('review_detail', pk=review.pk)
        else:
            messages.error(request, '請檢查表單內容是否正確。')
    else:
        form = ReviewForm()
    
    return render(request, 'restaurants_app/post.html', {'form': form})
