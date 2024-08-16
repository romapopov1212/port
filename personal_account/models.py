from django.db import models
from user.models import User
# Create your models here.
class Achievement(models.Model):
    STATUS_CHOICE = [
        ('u', 'Unverified'),
        ('v', 'Verified'),
        ('r', 'Rejected')
    ]

    name_achievement = models.CharField(max_length=200, null=False, unique=False)
    event_name = models.CharField(max_length=200, null=False, unique=False)
    link = models.CharField(max_length=255, null=False, unique=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, null=False, default='u', unique=False, choices=STATUS_CHOICE)
    points = models.IntegerField(null=False, default=0, unique=False)
    class Meta:
        db_table = 'achievement'

class Certificates(models.Model):
    image = models.ImageField(upload_to='certificates', null=False, unique=False)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)

    class Meta:
        db_table = 'сertificates'
