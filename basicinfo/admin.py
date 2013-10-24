from django.contrib import admin
from .models import *


class BasicInfoAdmin(admin.ModelAdmin):
    '''
    '''

admin.site.register(BasicInfo, BasicInfoAdmin)
