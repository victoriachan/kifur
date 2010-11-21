from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
from kifur.kifu_users.models import UserProfile

# Add our custom user profile fields to User Admin 
admin.site.unregister(User)
 
class UserProfileInline(admin.StackedInline):
    model = UserProfile
 
class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline]
 
admin.site.register(User, UserProfileAdmin)