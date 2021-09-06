from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    quote = models.TextField(max_length=1000, null=False, blank=False)
    team = models.CharField(max_length=100, null=True, blank=False)
    college = models.CharField(max_length=150, null=True, blank=False)

    def __str__(self):
        return f'{self.user.username} Profile'
        