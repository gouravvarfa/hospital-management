from django.contrib import admin
from .models import Medical

class medicalAdmin(admin.ModelAdmin):
      list_display=['name','contact','email','age','address','shop']

admin.site.register(Medical,medicalAdmin)
