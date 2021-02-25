from django.contrib import admin
from .models import Listings_display
# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','price','pub_date','realtor')
    list_display_links=('id','title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('id','title','zipcode','city')
    list_per_page = 20

admin.site.register(Listings_display,ListingAdmin)