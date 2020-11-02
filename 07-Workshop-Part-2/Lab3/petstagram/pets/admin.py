from django.contrib import admin
from .models import  Pet, Like

# Register your models here.
class LikeInline(admin.TabularInline):
    model = Like


class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name', 'age')
    list_filter = ('type', 'age')
    inlines = (
        LikeInline,
    )

admin.site.register(Pet, PetAdmin)