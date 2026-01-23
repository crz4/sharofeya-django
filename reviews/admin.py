from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_active')   # <-- исправлено
    list_filter = ('is_active',)
