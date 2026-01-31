from django.db import models

class Message(models.Model):
    user_text = models.TextField()
    bot_text = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User: {self.user_text[:20]}"
