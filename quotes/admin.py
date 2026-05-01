from django.contrib import admin
from .models import Category, Quote, Like


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['text_preview', 'author', 'category', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['text', 'author']
    fields = ['text', 'author', 'category', 'created_at']
    readonly_fields = ['created_at']

    def text_preview(self, obj):
        return obj.text[:100] + "..." if len(obj.text) > 100 else obj.text
    text_preview.short_description = "Citation"


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['quote_preview', 'session_id', 'created_at']
    list_filter = ['created_at']
    search_fields = ['quote__text', 'session_id']
    readonly_fields = ['created_at', 'quote', 'session_id']

    def quote_preview(self, obj):
        return obj.quote.text[:50] + "..."
    quote_preview.short_description = "Citation"
