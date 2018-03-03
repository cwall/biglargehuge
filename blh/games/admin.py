from django.contrib import admin
from blh.games.models import Games, Platform, Verdict, Review

class GamesAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	search_fields = ['title', 'platform']
	list_display = ('title', 'publish',)
	list_filter = ('title', 'platform', 'publish', )
	
class PlatformAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

class VerdictAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('verdict',)}
	list_display = ('verdict', )	

class ReviewAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('game', 'title', 'author', 'verdict', 'publish',)
	list_filter = ('game', 'title', 'publish', )
	
admin.site.register(Games, GamesAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(Verdict, VerdictAdmin)
admin.site.register(Review, ReviewAdmin)