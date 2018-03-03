from django.contrib import admin
from blh.gameify.models import Gameify, Season
from blh.guests.models import Guest

class GuestAdmin(admin.ModelAdmin):
	pass

class GuestInline(admin.TabularInline):
	model = Guest
	extra = 2
	
class SeasonAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('season',)}
	
class GameifyAdmin(admin.ModelAdmin):
	list_display = ('title', 'season')
	search_fields = ('title', 'season', 'guest')
	prepopulated_fields = {"slug": ("title",)}
	exclude = ('gameify_doc',)
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'author':
			kwargs['initial'] = request.user.id
			return db_field.formfield(**kwargs)
		return super(GameifyAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
            )
            	
admin.site.register(Gameify, GameifyAdmin)
admin.site.register(Guest, GuestAdmin)
admin.site.register(Season, SeasonAdmin)