from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
UserAdmin.list_display += ('koios_points',)  # don't forget the commas
UserAdmin.list_filter += ('koios_points',)
UserAdmin.fieldsets += (('koios_points', {'fields': ('koios_points',)}),)
admin.site.register(User, UserAdmin)
