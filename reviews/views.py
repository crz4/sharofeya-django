from django.shortcuts import render
from .models import Review


# reviews/views.py
def reviews(request):
    reviews = Review.objects.filter(is_active=True)
    return render(request, 'reviews/reviews.html', {
        'reviews': reviews
    })
