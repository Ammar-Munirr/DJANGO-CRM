from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

class User(AbstractUser):
    is_organisor = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)



class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class LeadModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    organization = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    agent = models.ForeignKey("Agent",null=True,blank=True,on_delete=models.SET_NULL)
    category = models.ForeignKey("category",related_name='leads',null=True,blank=True,on_delete=models.SET_NULL)


    def __str__(self):
        return self.first_name
    


class Category(models.Model):
    name = models.CharField(max_length=30)
    organization = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Agent(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    organization = models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
    

def createUserP(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)



post_save.connect(createUserP,sender=User)
