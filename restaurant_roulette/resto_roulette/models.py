from django.db import models
from django.contrib.auth.models import User
import json
# Create your models here.



class Business(models.Model):
    biz_name = models.CharField(max_length=25)
    biz_category = models.CharField(max_length=25)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.biz_name


class Business_Search(models.Model):
    biz_category = models.CharField(max_length=25)
    location = models.CharField(max_length=35)

    def __str__(self):
        return '%s %s %s' % (self.biz_category, ':', self.location)


class Queue(models.Model):
    biz_data = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def add(self, businesses):
        current_queue = json.loads(self.biz_data)
        current_queue.extend(businesses)
        self.biz_data = json.dumps(current_queue)
        self.save()
