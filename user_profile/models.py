from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

"""
Class in this model : 

Profile
"""


# Create your models here.
class Profile(models.Model):
    # Attributes
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    mobile_phone = models.CharField(max_length=20)
    office_phone = models.CharField(max_length=20)
    user_slack = models.CharField(max_length=255)
    # country choices
    Chile = 'CHILE'
    Mexico = 'MEXICO'
    Unassigned = 'UNASSIGNED'

    country_choices = (
        (Chile, 'CHILE'),
        (Mexico, 'MEXICO'),
        (Unassigned, 'UNASSIGNED'),
    )
    country = models.CharField(max_length=11, choices=country_choices)

    # Add model representation strings
    def __str__(self):
        return u'%s' % self.user

    # Meta class for the model.
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


# function create user profile
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=User)


# function save user profile
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()