from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default='default.png', upload_to='user_images')
    
    GENDER_CHOICES = (
        ('Male', 'Чоловіча стать'),
        ('Female', 'Жіноча стать'),
    )
    
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')
    is_delivery = models.BooleanField(default=False)

    def __str__(self):
        return f'Профіль {self.user.username}'