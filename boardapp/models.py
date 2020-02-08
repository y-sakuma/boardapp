from django.conf import settings
from django.db import models
from django.utils import timezone


class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    images = models.ImageField(upload_to='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    good = models.IntegerField(null=True, blank=True, default=0)
    readtext = models.CharField(max_length=100, null=True, blank=True, default='a')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
