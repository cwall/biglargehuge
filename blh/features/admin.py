from django.contrib import admin
from blh.features.models import Topic, Category, Feature, Rating, Content

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}

class ContentInline(admin.StackedInline):
	model = Content
	extra = 1

class TopicAdmin(admin.ModelAdmin):
		prepopulated_fields = {"slug": ("title",)}

class RatingAdmin(admin.ModelAdmin):
		prepopulated_fields = {"slug": ("rating",)}
				
class FeatureAdmin(admin.ModelAdmin):
	inlines = [
		ContentInline,
	]
	prepopulated_fields = {"slug": ("title",)}
	list_editable = ('category', 'date', 'slug', 'featured', 'publish')
	list_display = ('title', 'date', 'featured', 'publish', 'category', 'author', )
	list_filter = ('category', 'title', 'featured', 'publish', )
	date_hierarchy = 'date'
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'author':
			kwargs['initial'] = request.user.id
			return db_field.formfield(**kwargs)
		return super(FeatureAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
            )
	
	fieldsets = (
		(None, {
			'fields': ('author', 'category', 'title', 'subhead', 'body', 'date', 'cover' )
		}),
		
		('Audio options', {
			'classes': ('grp-collapse grp-closed collapse',),
			'fields': ('audio_file', 'audio_description', 'attachment')
		}),
		
		('Review options', {
			'classes': ('grp-collapse grp-closed collapse',),
			'fields': ('verdict', 'rating')
		}),
		
		('Meta options', {
			'classes': ('grp-collapse grp-closed collapse',),
			'fields': ('excerpt', 'feature_class', 'meta_keywords')
		}),
		
		('Related content options', {
			'classes': ('grp-collapse grp-closed collapse',),
			'fields': ('related_content', 'topics', 'url')
		}),
		
		('Sorting options', {
			'classes': ('wide',),
			'fields': ('tags', 'slug', 'featured', 'publish')
		}),
	)

admin.site.register(Category, CategoryAdmin)            
admin.site.register(Feature, FeatureAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Topic, TopicAdmin)