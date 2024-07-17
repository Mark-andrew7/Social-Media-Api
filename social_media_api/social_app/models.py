from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.TextField(max_length=300, blank=True)
  profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

