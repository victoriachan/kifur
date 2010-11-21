from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
# from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, related_name='user_profile')
    #user = models.OneToOneField(User)
    slug = models.SlugField(max_length=30, unique=True, null=True, verbose_name="url path")
    
    def __str__(self):  
          return "%s's profile" % self.user  

#def create_user_profile(sender, instance, created, **kwargs):
#    if created:  
#       profile, created = UserProfile.objects.get_or_create(user=instance)
#    post_save.connect(create_user_profile, sender=User)