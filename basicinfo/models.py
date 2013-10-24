from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BasicInfo(models.Model):
    '''
    Store basic info and XMl as such
    '''
    user = models.ForeignKey(User)
    xml = models.TextField(null=False)

    def __unicode__(self):
        return self.user

