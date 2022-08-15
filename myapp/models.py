from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Work(models.Model):
    SHIFT_TIMING=[
                ('Day Time', 'Day Time'),
                ('Night Time', 'Night Time')]
    project=models.CharField(max_length=50)
    task=models.CharField(max_length=50)
    team_member=models.CharField(max_length=50)
    shift_timing=models.CharField(max_length=20,choices=SHIFT_TIMING, default='Day Time')
    comments=models.CharField(max_length=250)
    def __str__(self):
        return f"{self.task}:{self.team_member}"

# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Registration.objects.create(user=instance)
#     instance.profile.save()

