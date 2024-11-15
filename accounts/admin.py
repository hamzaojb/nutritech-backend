from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'fullname', 'gender', 'is_active', 'is_admin')

admin.site.register(User, UserAdmin)
