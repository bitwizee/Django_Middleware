from django.db import models
from django.contrib.auth.models import User

class UserActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    is_address = models.GenericIPAddressField()
    path = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)


    
