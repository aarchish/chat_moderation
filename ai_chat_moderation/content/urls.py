# content/urls.py

from content.views import CommentView, FlaggedCommentsView
from django.urls import path

urlpatterns = [
    path("comment/", CommentView.as_view(), name="comment"),
    path("comments/flagged/", FlaggedCommentsView.as_view(), name="flagged-comments"),
]
# This code defines a URL pattern for the CommentView API endpoint. The CommentView handles POST requests to create new comments, including moderation checks using an external AI API.
# The URL pattern is registered under the path 'comment/' and is named 'comment' for easy reference in the Django application.
