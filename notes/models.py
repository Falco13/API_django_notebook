from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Note(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, null=True, blank=False, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated_at']
