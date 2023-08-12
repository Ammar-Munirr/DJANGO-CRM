from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

class User(AbstractUser):
    pass



class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class LeadModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    agent = models.ForeignKey("Agent",on_delete=models.CASCADE)


    def __str__(self):
        return self.first_name
    



class Agent(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    organization = models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
    

def createUserP(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)



post_save.connect(createUserP,sender=User)
