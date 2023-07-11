from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    userType = models.CharField(max_length=100, default='')

    class Meta:
        db_table = 'UserAPI'

