from django.db import models

# Create your models here.
# core/models.py
from django.db import models
import uuid
import secrets

class Photo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='photos/')
    email = models.EmailField()
    video = models.FileField(upload_to='videos/', blank=True, null=True)  # Nouveau champ pour vidéo
    secret_token = models.CharField(max_length=32, default=secrets.token_hex, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

class AnonymousComment(models.Model):
    photo = models.ForeignKey(Photo, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    audio = models.FileField(upload_to='comments_audio/', blank=True, null=True)