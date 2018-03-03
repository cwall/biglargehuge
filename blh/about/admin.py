from django.contrib import admin
from blh.about.models import About, Staff

class AboutAdmin(admin.ModelAdmin):
	pass

class StaffAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}
	
admin.site.register(About, AboutAdmin)
admin.site.register(Staff, StaffAdmin)