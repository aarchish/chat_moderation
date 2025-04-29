# content/serializer.py

from rest_framework import serializers
from content.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'flagged', 'created_at', 'moderation_labels']
        read_only_fields = ['flagged', 'created_at', 'moderation_labels']
