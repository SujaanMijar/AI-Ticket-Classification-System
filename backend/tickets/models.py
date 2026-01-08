from django.db import models

# Create your models here.
from django.db import models

class Ticket(models.Model):
    text = models.TextField()
    category = models.CharField(max_length=50)
    sentiment = models.CharField(max_length=20)
    priority = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category
