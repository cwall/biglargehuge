from django.contrib import admin
from blh.thebroadcast.models import Broadcast

class BroadcastAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'author':
			kwargs['initial'] = request.user.id
			return db_field.formfield(**kwargs)
		return super(BroadcastAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
            )
admin.site.register(Broadcast, BroadcastAdmin)