from django.db import models

# class UserActivity(models.Model):
#     nickname = models.CharField(max_length=255)
#     points = models.IntegerField()

#     def __str__(self):
#         return self.nickname

class Event(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateField()
    link = models.URLField()

    def __str__(self):
        return self.title