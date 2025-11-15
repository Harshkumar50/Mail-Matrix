from django.db import models
from django.contrib.auth.models import User


class Mail(models.Model):
    sender = models.ForeignKey(User, related_name="sent_mails", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="received_mails", on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return f"{self.subject} ({self.sender} → {self.receiver})"




