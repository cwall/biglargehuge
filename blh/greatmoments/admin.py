from django.contrib import admin
from blh.greatmoments.models import Gmig

class GmigAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	verbose_name = ['Great Moments']
	list_display = ('title', 'game', 'date', 'publish')
	list_filter = ('title', 'date', 'publish')
	
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'author':
			kwargs['initial'] = request.user.id
			return db_field.formfield(**kwargs)
		return super(GmigAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
            )
            	
admin.site.register(Gmig, GmigAdmin)

