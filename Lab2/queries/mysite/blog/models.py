from datetime import date, timedelta
from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class EntryManager(models.Manager):
    def published(self):
        """Return published entries (i.e., entries with a pub_date before today)."""
        return self.filter(pub_date__lt=date.today())

    def recent(self):
        """Return recent entries (i.e., published within the last 30 days)."""
        return self.filter(pub_date__gte=date.today() - timedelta(days=30))

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()

    objects = models.Manager()  # Default Manager
    entries = EntryManager()  # Custom Manager

    def __str__(self):
        return self.headline
