from django.db import models

class Rating(models.Model):
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)  # This is important

    def __str__(self):
        return f"Rating {self.rating}"
