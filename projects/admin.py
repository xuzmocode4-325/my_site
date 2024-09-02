from django.contrib import admin
from .models import Project, Review

# Register your models here.

# Customizing the Project admin view
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'updated_at', 'published']
    list_filter = ['author', 'updated_at', 'published']
    search_fields = ['name', 'description', 'content']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['-updated_at']

# Customizing the Reviews admin view
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'project', 'created_at', 'published']
    list_filter = ['project', 'user', 'created_at', 'published']
    search_fields = ['review']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Review, ReviewAdmin)