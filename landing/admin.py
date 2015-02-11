from django.contrib import admin
from landing.models import Toys
# Register your models here.

class ToysAdmin(admin.ModelAdmin):
    list_display = ('name','admin_thumbnail','price')
admin.site.register(Toys,ToysAdmin)