from django.contrib import admin

from .models import Item

admin.site.site_header = 'Tolly Administrator'
admin.site.site_title = 'Tolly Admininstator Area'
admin.site.index_header = 'Welcome to the Pollster Admin area'

admin.site.register(Item)