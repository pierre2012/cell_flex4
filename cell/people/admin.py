from models import *
from django.contrib import admin


class PersonAdmin(admin.ModelAdmin):
	list_display = ('name', 'member_type', 'admin_image', 'publications_name', 'sortorder')
	list_display_links = ('name',)
    # search_fields = ('name')


admin.site.register(Person,PersonAdmin)


