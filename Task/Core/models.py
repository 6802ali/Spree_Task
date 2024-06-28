from django.db import models

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    userName = models.CharField(max_length=20, unique=True)  # Adding unique constraint for username
    email = models.EmailField(max_length=50, unique=True)  # Using EmailField and unique constraint
    password = models.CharField(max_length=128)  # Increased max_length for better password storage

    def __str__(self):
        return self.userName

class Item(models.Model):
    user = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.TextField()
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name