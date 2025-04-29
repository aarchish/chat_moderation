from django.shortcuts import render

# Create your views here.

# content/views.py

import requests
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from content.utils import moderate_text
from content.models import Comment
from content.serializer import CommentSerializer

class CommentView(APIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Save the user and the text, and apply moderation
        user = self.request.user
        text = self.request.data.get("text", "")

        response = moderate_text(text) # Moderating the text using the Moderation MicroService with Hugging Face API 
        flagged_labels = response.get("labels", [])
        is_flagged = response.get("flagged", False)

        # Save the comment instance with the flagged status
        instance = serializer.save(user=user, flagged=is_flagged, moderation_labels=flagged_labels)

        # Optionally log the flagged comment for moderation
        if is_flagged:
            print(f"Comment by {user.username} flagged for moderation: {flagged_labels}")

    def post(self, request, *args, **kwargs):
        # Initialize serializer with incoming data
        serializer = CommentSerializer(data=request.data)
        
        if serializer.is_valid():
            # Perform the actual comment creation and moderation
            self.perform_create(serializer)
            
            # Return the created comment data with a possible moderation notice
            response = CommentSerializer(serializer.instance).data
            if response.get("flagged"):
                response["moderation_notice"] = "Your comment has been flagged for moderation."
            
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FlaggedCommentsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Retrieve all flagged comments
        flagged_comments = Comment.objects.filter(flagged=True)
        serializer = CommentSerializer(flagged_comments, many=True)
        return Response(serializer.data)
