from django.db import models
from django.contrib.auth.models import User

class Settings(models.Model):
	site_offline = models.BooleanField(default=False)
	site_name  = models.CharField(max_length=120, )
	
