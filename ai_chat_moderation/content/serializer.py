# content/serializer.py

from content.models import Comment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "text", "flagged", "created_at", "moderation_labels"]
        read_only_fields = ["flagged", "created_at", "moderation_labels"]
