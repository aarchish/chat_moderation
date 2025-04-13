# content/admin.py

from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'flagged', 'created_at')
    readonly_fields = ('moderation_labels',)
    search_fields = ('text', 'user__username')
    list_filter = ('flagged', 'created_at')
    ordering = ('-created_at',)
    actions = ['mark_as_flagged', 'unflag_comments']