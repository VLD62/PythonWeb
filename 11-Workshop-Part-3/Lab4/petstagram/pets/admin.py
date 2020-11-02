from django.contrib import admin
from .models import  Pet, Like, Comment
# Register your models here.

class LikeInLine(admin.TabularInline):
    model = Like

class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name', 'age')
    list_filter = ('type', 'age')
    inlines = (
        LikeInLine,
    )

admin.site.register(Pet, PetAdmin)
admin.site.register(Comment)