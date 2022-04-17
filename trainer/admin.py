from django.contrib import admin
from .models import Tag, Problem, ProblemInstance, TimeTaken

# Register your models here with the admin site.
@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('name','display_tag',)

@admin.register(ProblemInstance)
class ProblemInstanceAdmin(admin.ModelAdmin):
    list_display = ('problem','variables',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(TimeTaken)
class TimeTakenAdmin(admin.ModelAdmin):
    list_display = ('time',)