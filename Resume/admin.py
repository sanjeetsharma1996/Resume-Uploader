from django.contrib import admin
from .models import ResumeModel

@admin.register(ResumeModel)
class ResumeModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'name', 'email','dob', 'gender', 'locality', 'city', 'pin', 'mobile', 'state', 'job_city', 'profile_image', 'my_file']
