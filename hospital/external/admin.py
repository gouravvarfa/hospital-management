from django.contrib import admin
from .models import External

class externalAdmin(admin.ModelAdmin):
      list_display=['name','contact','email','age','address','shop']

admin.site.register(External,externalAdmin)
