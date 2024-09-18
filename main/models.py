from django.db import models
import uuid

class Products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama = models.CharField(max_length=255)
    harga = models.IntegerField()
    deskripsi = models.TextField()

    # namaMahasiswa = models.CharField(max_length=255)
    # npm = models.IntegerField()
    # kelas = models.CharField(max_length=255)

    # @property
    # def is_mood_strong(self):
    #     return self.mood_intensity > 5