from django.db import models
from django.contrib.auth.models import User

class save_result(models.Model):
    s_no = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    sentiment = models.CharField(max_length=20)
    confidence = models.FloatField('confidence')
    


