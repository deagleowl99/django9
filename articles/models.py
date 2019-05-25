from django.conf import settings
from django.db import models
from django.utils import timezone


class Article(models.Model):
    objects = models.Manager()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

    def get_excerpt(self):
        return self.text[:140] + "..." if len(self.text) > 140 else self.text
# Create your models here.
