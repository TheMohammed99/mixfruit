from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=150)
    profile_pic = models.ImageField(blank=True, null=True, default=None, upload_to='profile_pics')
    about = models.CharField(max_length=255, blank=True, null=True, default=None)
    facebook = models.URLField(blank=True, null=True, default=None)
    instagram = models.URLField(blank=True, null=True, default=None)
    twitter = models.URLField(blank=True, null=True, default=None)
    linkedin = models.URLField(blank=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f'{self.user.username} Profile'
    