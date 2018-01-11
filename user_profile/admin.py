from django.contrib import admin
from user_profile.models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ['user', 'country', 'address', 'mobile_phone', 'office_phone', 'user_slack']
