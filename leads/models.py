from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass



class LeadModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    agent = models.ForeignKey("Agent",on_delete=models.CASCADE)


    def __str__(self):
        return self.first_name
    



class Agent(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email