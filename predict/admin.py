from django.contrib import admin
from .models import Urllist
# Register your models here.

class UrllistModelAdmin(admin.ModelAdmin):
	list_display = ["id","title", "url"]
	#list_display_links = ["updated"]
	list_editable = ["title"]
	#list_filter = ["updated", "timestamp"]

	search_fields = ["title"]
	class Meta:
		model = Urllist


admin.site.register(Urllist, UrllistModelAdmin)
