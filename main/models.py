from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    descripton = models.TextField()

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5