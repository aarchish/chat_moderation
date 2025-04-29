from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    flagged = models.BooleanField(default=False)  # AI moderation flag
    created_at = models.DateTimeField(auto_now_add=True)
    moderation_labels = models.JSONField(default=list, null=True, blank=True)  # Store moderation labels as a list

    def __str__(self):
        return f"{self.user.username}: {'[FLAGGED] ' if self.flagged else ''}{self.text[:50]}"