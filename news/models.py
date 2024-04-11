from django.db import models
from django.utils import timezone

class News(models.Model):
    title = models.CharField(max_length=255, unique=True, default='')
    content = models.TextField(default='')
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.title