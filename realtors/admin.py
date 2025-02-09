from django.contrib import admin
from .models import Agents
# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','hire_date')
    list_display_links = ('id','name')
    search_fields = ('name',)
admin.site.register(Agents,RealtorAdmin)