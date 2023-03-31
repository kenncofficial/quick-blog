from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import PreRegistration
# Register your models here.
@admin.register(PreRegistration)
class PreRegistrationAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name']
