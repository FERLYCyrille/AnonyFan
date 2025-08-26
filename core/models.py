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

    secret_token = models.CharField(max_length=32, default=secrets.token_hex, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

class AnonymousComment(models.Model):
    photo = models.ForeignKey(Photo, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
