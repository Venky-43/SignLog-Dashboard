from django.db import models

class Signup(models.Model):
    USER_TYPE_CHOICES = (
        ('Patient', 'Patient'),
        ('Doctor', 'Doctor'),
    )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.jpg')
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    address_line1 = models.CharField(max_length=255, default='Not Provided')
    city = models.CharField(max_length=50,default='Not Provided')
    state = models.CharField(max_length=50,default='Not Provided')
    pincode = models.CharField(max_length=10,default='Not Provided')
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='Patient')

class Login(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.username} ({self.user_type})"

# Create your models here.
